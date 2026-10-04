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


# utility function
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
     with open("patients.json", "w") as f:
        json.dump(data, f)


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

# SAME CODE I HAVE WRITTEN IN , main.py file.. keeping here just for reference, 
# run "uvicorn main:app --reload" in terminal and visit "http://127.0.0.1:8000/docs" to perform create operation playing with "/create" endpoint