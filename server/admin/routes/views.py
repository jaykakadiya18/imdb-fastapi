from fastapi import APIRouter, Body, Request, HTTPException, status, Depends
from typing import List
from fastapi.security import HTTPBearer
from server.admin.models.schema import (
     UserSchema, UserLoginSchema, Token
)
from server.admin.models.database import (
    fetch_user, create_user
)
# from server.auth.auth_handler import signJWT, decodeJWT
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

import time
import jwt

JWT_SECRET = '944ca420b8c316cabcd1885e9de6849f2350d1d29fa9d4f38fd8de33d4a31246'
JWT_ALGORITHM = 'HS256'

def token_response(token: str):

    return {"access_token": token}


def signJWT(user_id: str, role: str):
    """
    Token expire in 30 mins
    """

    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + 1800
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str):

    """Decoding JWT TOken with the hlp of secret key and hashing algorithm
    """
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token["expires"] >= time.time(): 
            return decoded_token
    except:
        return {}

router = APIRouter()
class JWTBearer(HTTPBearer):

    """A handler class to verify the authenticity of the authorization header
    """
    
    def __init__(self, allowed_roles: List = [], auto_error: bool = True):
        self.allowed_roles = allowed_roles
        super(JWTBearer, self).__init__(auto_error=auto_error)

    def verify_jwt(self, jwtoken: str): #the header payload

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        return payload

Auth_handler = JWTBearer([])


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_description="Authorization Token", response_model=Token)
async def signup(user_data: UserSchema):
    # Check if email address already exists in database
    user = await fetch_user({'email': user_data.email})
    if user:
        raise HTTPException(status_code=409, detail="User already registered.")
    # Create user
    signedup_user = await create_user(user_data)
    # Generate JWT Access token
    return signJWT(signedup_user['user_id'], signedup_user['role'])
   

@router.post("/login", response_description="Authorization Token", response_model=Token)
async def user_login(UserData: UserLoginSchema = Body(...)):
    user = await fetch_user({'email': UserData.email}, True)
    # Verify password
    if verify_password(UserData.password, user['hashed_password']):
        return signJWT(user['user_id'], user['role'])



