from pydantic import BaseModel, computed_field

class Patient(BaseModel):

    name: str
    weight: float # kgs
    height: float # meters

    @computed_field
    @property
    def calculated_bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.height)
    print(patient.weight)
    print("BMI >>>", patient.calculated_bmi)
    # the name "calculated_bmi" here should be same as function name we have written above (line 12)

patient_info = {
    'name':'Vaibhav', 
    'weight': 75.2, 
    'height': 1.72,
    }

patient1 = Patient(**patient_info) 

update_patient_data(patient1)