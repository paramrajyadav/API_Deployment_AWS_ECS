# main.py

from fastapi import FastAPI
from aux_function import add_numbers, concatenate_strings  # Ensure you have the correct import
from pydantic import BaseModel

# Define request models
class AddRequest(BaseModel):
    num1: float
    num2: float

class ConcatenateRequest(BaseModel):
    str1: str
    str2: str

# Initialize FastAPI app
app = FastAPI()

# Welcome page endpoint
@app.get("/")
async def welcome():
    return {"message": "Welcome to the FastAPI app! Use the /add endpoint to add two numbers and /concatenate to combine two strings."}

# Endpoint to add two numbers
@app.post("/add")
async def add(request: AddRequest):
    result = add_numbers(request.num1, request.num2)
    return {"result": result}

# Endpoint to concatenate two strings
@app.post("/concatenate")
async def concatenate(request: ConcatenateRequest):
    result = concatenate_strings(request.str1, request.str2)
    return {"result": result}

# Run the app using: uvicorn main:app --reload



# from fastapi import FastAPI

# # Initialize FastAPI app
# app = FastAPI()

# # Welcome page endpoint
# @app.get("/")
# async def welcome():
#     return {"message": "Welcome to the FastAPI app!"}

# # Run the app using: uvicorn main:app --reload

