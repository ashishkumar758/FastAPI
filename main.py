from fastapi import FastAPI
app=FastAPI()

# Querry parameter user?name="ashish"

@app.get("/users")
def get_users(name):
    return {"Name":name}

# Querry parameter if it is not that given then it will return None

@app.get("/task")
def get_task(name:str = None):
    return {"Name":name}

# Default parameter

@app.get("/product")
def get_product(name : int = 10):
    return {"name" : name}

# Default items

@app.get("/items")
def get_items(name:str = None, count : int = 10):
    return {
        "name":name,
        "count":count
    }