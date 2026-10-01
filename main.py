from fastapi import FastAPI
from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     password:str

# class UserResponse(BaseModel):
#     name:str
#     age:int
# @app.get("/user", response_model=UserResponse)
# def get_user():
#     return{
#         "name":"Ashish",
#         "age":21,
#         "password":"12345678"
#     }

app = FastAPI()
class User(BaseModel):
    name:str
    age:int
    password:str
class ResponseUser(BaseModel):
    name:str
    age:int

@app.get("/user", response_model=User)
def get_user():
    return{
        "name":"Ashish",
        "age":21,
        "password":"123456"
    }