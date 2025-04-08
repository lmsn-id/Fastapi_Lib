from fastapi import Header, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED
import os
from dotenv import load_dotenv

load_dotenv() 

API_KEY = os.getenv("API_KEY")

def check_api_key(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Error Sistem")

    token = authorization.split(" ")[1]
    if token != API_KEY:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Error Sistem")
