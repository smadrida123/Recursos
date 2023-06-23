#Python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional
import json

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#Models

class UserBase(BaseModel):
    user_id:UUID=Field(...)
    email: EmailStr=Field(...)

class UserLogin(UserBase):
    password:str=Field(
        ...,
        min_length=8,
        max_length=30
    )
class User(UserBase):
    first_name:str=Field(
        ...,
        min_length=2,
        max_length=30)
    last_name:str=Field(
        ...,
        min_length=2,
        max_length=30
        )
    birth_date:Optional[date]=Field(default=None)


class Tweet(BaseModel):
    tweet_id:UUID=Field(...)
    content:str=Field(
        ...,
        min_length=1,
        max_length=256
        )
    created_at:datetime=Field(default=datetime.now())
    updated_at:Optional[datetime]=Field(default=None) 
    by:User=Field(...)    

class UserRegister(User, UserLogin):
    
    pass

class UserExists(BaseModel): 
    email: EmailStr = Field(...)
    message: str = Field(default="User exists!")


#HELPFUL FUNCTIONS
##Read file
def read_data(file1):
    with open("{file1}.json","r+", encoding="utf-8") as f:
        return json.load(f)
    
def serialize(d):
    for key in d:
        val = d[key]
        # For nested objects
        if type(val) is dict:
            serialize(val)
            continue
        if type(val) in [UUID, datetime, date]:
            d[key] = str(val)
    return d

