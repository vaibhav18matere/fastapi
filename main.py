from fastapi import FastAPI, HTTPException, Path
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