from typing import Union,List

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1,name="jung",age=23),
    Person(id=2,name="nyima",age=33)
]

@app.get("/api")
def read_root():
    return DB

