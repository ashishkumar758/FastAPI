from fastapi import FastAPI
app=FastAPI()
# Home route
@app.get("/")
def home():
    return {"message":"This is home route."}

#Dynamic routing
#users task
from fastapi import FastAPI
@app.get("/tasks/{task_id}")
def get_task_id(task_id):
    return {"task id":task_id}

#Dynamic routing based on datatypes
@app.get("/users/{user_id}")
def get_user_id(user_id:int):
    return {"User id":user_id}

