#Python
from typing import Optional
from enum import Enum
import re
#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import PaymentCardNumber
#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path
from fastapi import status 


app=FastAPI()

#Models
class HairColor(Enum):
    white="white"
    brown="brown"
    blonde="blonde"
    black="black"
    red="red"

class PersonBase(BaseModel):
    first_name:str=Field(
     ...,
     min_length=1,
     max_length=50
     #example="Oreo"
     )
    last_name:str=Field(
     ...,
     min_length=1,
     max_length=50
     )
    age:int=Field(
     ...,
     gt=0,
     le=115
    )
    hair_color1:Optional[HairColor]=Field(default=None)
    is_married:Optional[bool]=Field(default=None)
    email:EmailStr=Field(
        ...,
        title="Email",
        description="Enter person email. Required"
    )
    paymentcardnumber:PaymentCardNumber=Field(
        ...,
        title="Payment Card Number",
        description="Enter credit card number. Required"
    )

class Person(PersonBase):
    password:str=Field(
        ...,
        min_length=8
    )

class PersonOut(PersonBase):
    pass
   
"""
 class Config:
        schema_extra={
            "example":{
                "first_name":"Santiago",
                "last_name":"Madrid",
                "age":23,
                "hair_color":"red",
                "is_married":"True",
                "email":"santiago@ejemplo.com",
                "paymentcardnumber":"123456789007"
            }
        }"""

class Location(BaseModel):
    city:str=Field(...,
     min_length=1,
     max_length=50
     )
    state:str=Field(...,
     min_length=1,
     max_length=50
     )
    country:str=Field(...,
     min_length=1,
     max_length=50
     )
    class Config:
        schema_extra={
            "example":{
                "city":"Manizales",
                "state":"Caldas",
                "country":"Colombia"
            }
        }

#PATH OPERATION
#1) PATH OPERATION DECORATOR:
@app.get(
    path="/",
    status_code=status.HTTP_200_OK
    )
#2) PATH OPERATION FUNCTION
def home():
    return {"Hello":"World"}

@app.get("/items/{num_item}")
def items(num_item):
    return {"num_item":num_item}

#REQUEST AND RESPONSE BODY
#Para recibir de parte de usuario el objeto persona se necesita un request body
@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED
    )
def create_person(person:Person=Body(...)):
     return person

#validaciones: Query parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK
    )
def show_person(
    name: Optional[str]=Query(
        None,
        min_length=1,
        max_length=50,
        title="Name",
        description="Person Name. Between 1-50 characters",
        example="Oreo"
        ),
    age:int=Query(
        ...,
        gt=0,
        title="Age",
        description="Person Age. Obligatory",
        example="7"
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
        description="This is the person id. Required",
        example=1
        )
):
 return {person_id:"It exists!"}

 #Validaciones: Request body
@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_202_ACCEPTED
    )
def update_person(
    person_id:int=Path(
        ...,
        ge=1,
        title="Person id",
        description="This is the person id. Required",
        example=1
        ),
    person:Person=Body(...),
    location:Location=Body(...)
 ):
  results=person.dict()
  results.update(location.dict())
  return results

