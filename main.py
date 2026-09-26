from fastapi import FastAPI
# we use pyndatic to add validation in dictionary or it is defined as schema desgin for the user so that he get to know about how many field he has to fill or of which data type.
from pydantic import BaseModel
app = FastAPI()
class Users(BaseModel):
    name:str
    age:int
@app.post("/create-user")
def create_user(user:Users):
    return{
        "message":"User data",
        "Data":user
    }