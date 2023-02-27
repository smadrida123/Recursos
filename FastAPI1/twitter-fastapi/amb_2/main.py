#FastAPI
from fastapi import FastAPI

#Modelos
from models import UserBase, UserLogin, User, Tweet

app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}