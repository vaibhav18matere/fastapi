from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted patient data")

def update_patient_date(patient:Patient):
    patient.age = 90
    print(patient.age)
    print("updated patient data")

patient_info = {
    "name": "Vaibhav",
    "age": 28
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_date(patient1)