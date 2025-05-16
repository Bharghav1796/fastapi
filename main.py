# from typing import Optional
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# def read_root(name: Optional[str] = None):
#     if name:
#      return {"message": f"Hello {name}"}
#     return {"message": "Hello World"}

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model for POST requests
class User(BaseModel):
    name: str
    age: Optional[int] = None

@app.get("/")
def read_root(name: Optional[str] = None):
    if name:
        return {"message": f"Hello {name}"}
    return {"message": "Hello World"}

# POST endpoint
@app.post("/submit")
def submit_user(user: User):
    return {"message": f"Received user {user.name}, age {user.age}"}


