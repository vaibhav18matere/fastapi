from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel # for data validation
from typing import List # for data type
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

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
def view_patient(patient_id: str = Path(..., description = "The ID of the patient in the DB", example = "P001", min_length = 4, max_length = 4)): 
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
