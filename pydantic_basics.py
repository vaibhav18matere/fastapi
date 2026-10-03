from operator import gt
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str = Field(min_length=2, max_length=50, description="Name of the patient", example="Vaibhav")
    age: int
    married: bool = False    # default value is False if not provided
    email: EmailStr
    medications: List[str]
    allergies: Optional[Dict[str, str]] = None
    website: AnyUrl
    weight: float = Field(gt=0, lt=100, description="Weight in kg", example=70.5)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.medications)
    print(patient.allergies)
    print(patient.email)
    print(patient.website)
    print(patient.weight)
    print("inserted patient data >>>>>>>>>>>>>>>>>>>>")

def update_patient_date(patient:Patient):
    patient.age = 90
    print(patient.age)
    print(patient.married)
    print(patient.medications)
    print(patient.allergies)
    print(patient.website)
    print(patient.weight)
    print("updated patient data >>>>>>>>>>>>>>>>>>>>")

patient_info = {
    "name": "Vaibhav",
    "age": 28,
    "married": True,
    "medications": ["Aspirin", "Ibuprofen"],
    "allergies": {"penicillin": "moderate", "latex": "moderate"},
    "email": "abc@gmail.com",
    "website": "https://www.google.com",
    "weight": 99
    # if we remove allergies, it will be None
    # check with www.googlecom
    # check with -10
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_date(patient1)