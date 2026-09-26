from fastapi import FastAPI
app=FastAPI()
# Home route
@app.get("/")
def home():
    return {"message":"This is home route."}

# About route
@app.get("/about")
def about():
    return {"message":"This is about route."}

#users route
@app.get("/users")
def users():
    return {"message":["Mohit","Rohit","Amit"]}