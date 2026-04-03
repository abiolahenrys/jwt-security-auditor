from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
import datetime


app = FastAPI(title="Vulnerable jwt api", description="for security testing purposes only")


SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    username: str
    password: str

def create_token(username: str):
    payload = {
        "username": username,
        "role": "user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


@app.post("/login")
def login(login_req: LoginRequest):
    token = create_token(login_req.username)
    return{"token": token, "username": login_req.username}


@app.get("/")
def root():
    return {"message": "Welcome to the vulnerable jwt api. Try /login and /user/me later."}