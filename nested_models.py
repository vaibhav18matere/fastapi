from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address : Address  # here type is Address and not str, int etc

address_dict = {
    "city" : "Pune",
    "state" : "Maharashtra",
    "pin" : "422201"
}

address1 = Address(**address_dict)

patient_dict = {
    "name" : "Vaibhav",
    "age" : 26,
    "gender" : "Male",
    "address" : address1
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

# Benefitts
# 1. Better Organization of related data
# 2. Reusability 
# 3. Readability
# 4. Validation