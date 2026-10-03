from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    married: bool = False    # default value is False if not provided
    email: EmailStr
    medications: List[str]
    allergies: Optional[Dict[str, str]] = None
    website: AnyUrl

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.medications)
    print(patient.allergies)
    print(patient.email)
    print(patient.website)
    print("inserted patient data >>>>>>>>>>>>>>>>>>>>")

def update_patient_date(patient:Patient):
    patient.age = 90
    print(patient.age)
    print(patient.married)
    print(patient.medications)
    print(patient.allergies)
    print(patient.website)
    print("updated patient data >>>>>>>>>>>>>>>>>>>>")

patient_info = {
    "name": "Vaibhav",
    "age": 28,
    "married": True,
    "medications": ["Aspirin", "Ibuprofen"],
    "allergies": {"penicillin": "moderate", "latex": "moderate"},
    "email": "abc@gmail.com",
    "website": "https://www.google.com"
    # if we remove allergies, it will be None
    # check with www.googlecom
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_date(patient1)