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
import os

app = FastAPI()

# Data model for POST requests
class User(BaseModel):
    name: str
    age: Optional[int] = None

# GET endpoint with optional query param
@app.get("/")
def read_root(name: Optional[str] = None):
    if name:
        return {"message": f"Hello {name}"}
    return {"message": "Hello World"}

# POST endpoint
@app.post("/submit")
def submit_user(user: User):
    return {"message": f"Received user {user.name}, age {user.age}"}

# Optional: To run locally or from Python directly
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Use $PORT if set, otherwise 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)
