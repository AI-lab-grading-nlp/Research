from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

class UserInput(BaseModel):
    operation: str
    x: float
    y: float

app = FastAPI()

@app.post('/calculate')
def operate(input:UserInput):
    result = calculate(input.operation, input.x, input.y)
    return result
