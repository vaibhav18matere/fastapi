from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

# Problem Statement 1 : You have to allow only specified official emails as a input 

    @field_validator('email')
    @classmethod
    def email_validator(cls, email_value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = email_value.split('@')[-1]
        print("domain name >>>", domain_name)

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return email_value

def update_patient_data(patient: Patient):

    print("valid email >>>>", patient.email)

patient_info = {
    'name':'nitish', 
    'email':'abc@hdfc.com', 
    # here try adding diff email ids abc@xyz.com
    'age': '30', 
    'weight': 75.2, 
    'married': True, 
    'allergies': ['pollen', 'dust'], 
    'contact_details':{'phone':'2353462'}
    }

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)