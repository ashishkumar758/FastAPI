from fastapi import FastAPI,HTTPException, Request
from fastapi.responses import JSONResponse
app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name=name

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request, exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"user {exc.name} not found"
        }
    )
@app.get("/users/{name}")
def get_user(name:str):
    if name != "mohit":
        raise UserNotFoundException(name)
    return{
        "name":name
    }