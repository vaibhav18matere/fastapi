from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field, computed_field # for data validation
from fastapi.responses import JSONResponse
from typing import List, Annotated, Literal, Optional
import json # for data type

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

# calculate BMI dynamically based on the height and weight given i/p fields

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

# calculate verdict based on BMI calculated

    @computed_field
    @property
    def verdict_calc(self) -> str:
        bmi = self.bmi

        if bmi < 18.5:
            return "Underweight"
        if bmi < 25:
            return "Normal"
        if bmi < 30:
            return "Overweight"
        return "Obese"

# UPDATE - we have to create new class because user can edit or all fields, we never know and i above modal "class Patient(BaseModel):"
# all fields are mandatory. in edit those fields are optional to edit
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]
# all default values are set as None

# utility function
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
     with open("patients.json", "w") as f:
        json.dump(data, f)

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas:List[Tea] = [] # list of teas

# "Decorators" - gives superpower to the function

@app.get("/")
def read_root():
    return {"message": "Welcome to tea house"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def create_new_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea.id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"error": "Tea not found"}

@app.get('/view')
def view():
    data = load_data()
    return data

# to find a particular patient, we can use the path parameter in the URL. The path parameter is defined in the route using curly braces {}. In this case, we are defining a path parameter called patient_id.

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description = "The ID of the patient in the DB", examples = "P001", min_length = 4, max_length = 4)): 
    # load all patients data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        return HTTPException(status_code=404, detail="Patient not found")

# check the resource at http://127.0.0.1:8000/patient/P001

# QWERY PARAMETERS - to sort the patients by height, weight or bmi. The query parameters are defined in the route using the Query class. In this case, we are defining two query parameters called sort_by and order.

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = "The field to sort the patients by height, weight or bmi"), order: str = Query('asc', description = "The order to sort the patients by asc or desc")):
    valid_fields = ['height', 'weight', 'bmi']
    valid_orders = ['asc', 'desc']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")
    if order not in valid_orders:
        raise HTTPException(status_code=400, detail="Invalid order. Valid options are: asc, desc")
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)
    return sorted_data

# check the resource at http://127.0.0.1:8000/sort?sort_by=height , http://127.0.0.1:8000/sort?sort_by=weight , http://127.0.0.1:8000/sort?sort_by=bmi
# http://127.0.0.1:8000/sort?sort_by=bmi&order=desc , http://127.0.0.1:8000/sort?sort_by=height&order=desc


@app.post("/create")
def create_patient(patient:Patient):
    data = load_data()     # load existing data
    if patient.id in data:     # check if the existing patient exists
        raise HTTPException(status_code=400, detail="Patient already exists!")
    # if not then add new user in DB
    # note : here data = load_data() is a python dictionary and patient:Patient is a pydantic object
    # we have to add in existing data in pydanctic object so,
    data[patient.id] = patient.model_dump(exclude="id")
    # save into json file
    save_data(data)
    print("check create patient endpoint")
    return JSONResponse(status_code=201, content={"message":"Patient Created Succssfully!"})

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if(patient_id not in data):
        raise HTTPException(status_code=404, detail="Patient Not Found!")

    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    # exclude_unset=True because i only want those fields which client sent me to change.

    existing_patient_info.update(updated_patient_info)  # updating values sent by client in {}
    
    # data[patient_id] = existing_patient_info
    # we can directly do this but if user changes weight or height, BMI and verdict changes dynamically.
    # so we need to handle that case as well.
    # we will convert "existing_patient_info" => to "pydantic object" => so that new values of BMI and verdict will be calculated dynamically.
    # then we will coonverted Pydantic object into dict and save the data.
    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info) #here in {} we do not have ID (check patient json) so we have added id in previous line

    #pydantic object => dict
    existing_patient_info = patient_pydantic_object.model_dump(exclude="id")

    # add this dict to data
    data[patient_id] = existing_patient_info 

    # save new data
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "User Updated!"})


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not Found!")

    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=202, content={"message": "Patient Deleted!"})