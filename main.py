from fastapi import FastAPI # it is aframework
from pydantic import BaseModel # for data validation
from typing import List # for data type

app = FastAPI()

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