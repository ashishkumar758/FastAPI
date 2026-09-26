from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Address(BaseModel):
    city:str
    pincode:int
class Users(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/create_user")
def create_user(user:Users):
    return{
        "message":"User created",
        "data":user,
    }