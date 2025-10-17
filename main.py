from fastapi import FastAPI
import requests
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI(title="Dynamic Profile Endpoint")

class UserInfo(BaseModel):
    email: EmailStr
    name: str
    stack: str

class Profile(BaseModel):
    status: str = "success"
    user: UserInfo
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    fact: str
    
    class Config:
        from_attributes = True

def get_cat_fact():

    url = os.getenv("CAT_FACT_URL")
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        return res.json()["fact"]
    except Exception as e:
        return f"Could not fetch cat fact: {str(e)}"

@app.get("/")
def root():
    return {"message": "Dynamic Profile Endpoint"}


@app.get("/me")
def profile():

    user = UserInfo(email="itsemekaeze903@gmail.com", name="Emmanuel Eze", stack="Python/Fastapi")

    profile = Profile(user=user, fact=get_cat_fact())
    return {
        "status": profile.status,
        "user": profile.user,
        "timestamp": profile.timestamp,
        "fact": profile.fact
    }