from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address : Address

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


temp_container =  patient1.model_dump()
print(temp_container)
print(type(temp_container))   # dict


temp_container2 = patient1.model_dump_json()

print(temp_container2)
print(type(temp_container2))  # json 

# include, exclude

temp_container3 = patient1.model_dump(include="name")
print(temp_container3) # we will only get {'name': 'Vaibhav'}