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
from fastapi import Form
from fastapi import Header
from fastapi import Cookie
from fastapi import status 
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException


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
   
class LoginOut(BaseModel):
    username:str=Field(...,max_lenght=20,example="oreo")
    message:str=Field(default="Login succesfully!")
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
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    summary="Home of the app"
    )
#2) PATH OPERATION FUNCTION
def home():
    """
    HOME

    Welcome of the home of the app!.

    Parameters: None

    Returns a hello world in JSON on this endpoint

    """
    return {"Hello":"World"}

@app.get(
    path="/items/{num_item}",
    tags=["General"],
    summary="Number of items"
    )
def items(num_item):
    """
    Number of items
    
    This path operation shows the number of items indexed at the path operator
    
    Parameters: 
    - Number of items: **path operator (type: number)** indexed after endpoint /items
    
    Returns JSON format of type {num_items:path operator indexed by user}
    """
    return {"num_item":num_item}

#REQUEST AND RESPONSE BODY
#Para recibir de parte de usuario el objeto persona se necesita un request body
@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Create person in the app"
    )
def create_person(person:Person=Body(...)):
     """
     Create person

     This path operation creates a Person in the app and save the information in the database

     Parameters: 
     - Request body parameter:
       - **person: Person** -> A person model with first name, last name, age, hair color, marital status, email and payment card number
     
     Returns a person model with first name, last name, age, hair color, marital status, email and payment card number
     """
     return person

#validaciones: Query parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="Name & age",
    deprecated=True
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
 """
 Name & age

 Shows the person´s name (optional) and its age (obligatory)

 Parameters=
  - Name (Query parameter): Optional. Inmediatly after endpoint detail  -> example: name=""
  - Age (Path parameter): Obligatory. after endpoint detail if name is not indexed or after parameter name using "&" -> example: age=""

 Returns JSON format type {"name":"age"}

 """
    
 return {name:age}

#Validaciones: Path parameters

persons=[1,2,3,4,5]

@app.get(
    path="/person/detail/{person_id}",
    tags=["Persons"],
    summary="Person´s ID Checker"
    ) 
def show_person(
    person_id:int=Path(
        ...,
        ge=1,
        title="Person_id",
        description="This is the person id. Required",
        example=1,
        summary="Person´s Id"
        )
):
 """
 Person ID

 Shows if the ID of a person exists

 Parameters: 
  - Person_ID: Path parameter **type:Number**

 Returns JSON format with assurance of existance of the ID indexed
 
 """
 if person_id not in persons:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="This person does not exist"
    )
 
 return {person_id:"It exists!"}

 #Validaciones: Request body
@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Persons"]
    )
def update_person(
    person_id:int=Path(
        ...,
        ge=1,
        title="Person id",
        description="This is the person id. Required",
        example=1,
        summary="Update person"
        ),
    person:Person=Body(...),
    location:Location=Body(...)
 ):
 """
 Update person

 it updates the person information regarding its information and location

 Parameters:
  - Path parameter: Person Id **type: integer**
  -Request body parameter:
     **person: Person** -> A person model with first name, last name, age, hair color, marital status, email and payment card number
     **location: Location** -> A loction model with city, state and country

Returns JSON format of info of person and location models (person and location models)


 """
 results=person.dict()
 results.update(location.dict())
 
 return results

#Forms - Formularios

@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="Login"
)
def login(username:str=Form(...),password:str=Form(...)):
    """
    Login

    It collects username and password from user

    Parameters: None
    Fill information in formulary

    Returns JSON format with username and welcome message if logged succesfully
    """
    return LoginOut(username=username)

#Cookies and Headers Parameters
@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["Form"],
    summary="Contact form"
)
def contact(
    first_name:str=Form(
        ...,
        max_length=30,
        min_length=2
    ),
    last_name:str=Form(
        ...,
        max_length=30,
        min_length=2
    ),
    email:EmailStr=Form(...),
    message:str=Form(
        ...,
        min_length=15
    ),
    user_agent:Optional[str]=Header(default=None),
    ads:Optional[str]=Cookie(default=None)
):
   """
   Contact Form

   It collects info and message from user in form

   Parameters:
   - user-agent (Optional)
   - ads (Optional)
   - Request body parameters(Obligatory)
     -first name
     -last name
     -email
     -message

   it returns header parameter
   """
   return user_agent

#files and upload files
@app.post(
    path="/post-image",
    tags=["update"],
    summary="Post image"
)
def post_image(
    image:UploadFile=File(...)
):
   """
   Post Image

   It lets the user upload an image and know its info

   Parameters: None

   it returns info (name, format and size) of the image that was uploaded by user
   """
   return {
    "Filename":image.filename,
    "Format":image.content_type,
    "Size(kb)":round(len(image.file.read())/1024,ndigits=2)
   }