from typing import Optional, Dict, List
from pydantic import BaseModel, EmailStr, Field

class Token(BaseModel):
    access_token: Optional[str]

class UserInDB(BaseModel):
    hashed_password: str
    email: EmailStr = Field(...)
    fullname: str = Field(...)
    user_id: str = Field(...)
    role: str = Field(...)

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Jay Kakadiya",
                "email": "jaykakadiya2014@gmail.com",
                "password": "123456"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(Ellipsis)
    password: str = Field(Ellipsis)

    class Config:
        schema_extra = {
            "example": {
                "email": "jaykakadiya2014@gmail.com",
                "password": "123456"
            }
        }

