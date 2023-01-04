#Python
from typing import Optional
#Pydantic
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

app=FastAPI()

#Models
class Person(BaseModel):
    fisrt_name:str
    last_name:str
    age:int
    hair_color:Optional[str]=None
    is_married:Optional[bool]=None

class Location(BaseModel):
    city:str
    state:str
    country:str
#PATH OPERATION
#1) PATH OPERATION DECORATOR:
@app.get("/")
#2) PATH OPERATION FUNCTION
def home():
    return {"Hello":"World"}

@app.get("/items/{num_item}")
def items(num_item):
    return {"num_item":num_item}

#REQUEST AND RESPONSE BODY
#Para recibir de parte de usuario el objeto persona se necesita un request body
@app.post("/person/new")
def create_person(person:Person=Body(...)):
     return person

#validaciones: Query parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str]=Query(
        None,
        min_length=1,
        max_length=50,
        title="Name",
        description="Person Name. Between 1-50 characters"
        ),
    age:int=Query(
        ...,
        gt=0,
        title="Age",
        description="Person Age. Obligatory"
        )
):
 return {name:age}

#Validaciones: Path parameters
@app.get("/person/detail/{person_id}") 
def show_person(
    person_id:int=Path(
        ...,
        ge=1,
        title="Person_id",
        description="This is the person id. Required"
        )
):
 return {person_id:"It exists!"}

 #Validaciones: Request body
@app.put("/person/{person_id}")
def update_person(
    person_id:int=Path(
        ...,
        ge=1,
        title="Person id",
        description="This is the person id. Required"
        ),
    person:Person=Body(...),
    location:Location=Body(...)
 ):
  results=person.dict()
  results.update(location.dict())
  return results

