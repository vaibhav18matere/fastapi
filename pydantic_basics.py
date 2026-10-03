from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    married: bool
    medications: List[str]
    allergies: Optional[Dict[str, str]] = None

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.medications)
    print(patient.allergies)
    print("inserted patient data >>>>>>>>>>>>>>>>>>>>")

def update_patient_date(patient:Patient):
    patient.age = 90
    print(patient.age)
    print(patient.married) = False # default value is False if not provided
    print(patient.medications)
    print(patient.allergies)
    print("updated patient data >>>>>>>>>>>>>>>>>>>>")

patient_info = {
    "name": "Vaibhav",
    "age": 28,
    "married": True,
    "medications": ["Aspirin", "Ibuprofen"],
    "allergies": {"penicillin": "moderate", "latex": "moderate"}
    # if we remove allergies, it will be None
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_date(patient1)