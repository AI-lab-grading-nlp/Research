from fastapi import FastAPI
from pydantic import BaseModel
from ngram import ngramize
import json

class UserInput(BaseModel):
    hc_lo: str
    grade: float
    n: float

class UserInput2(BaseModel):
    crap: str


app = FastAPI()

@app.post('/ngram')
def operate(input:UserInput):
    result = ngramize(input.hc_lo, input.grade, input.n)
    return result


@app.post('/try')
def work(input:UserInput2):
    result = 'crap'
    return result

