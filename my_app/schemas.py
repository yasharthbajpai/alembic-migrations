from pydantic import BaseModel, EmailStr
from typing import Optional

# Pydantic models for API request/response validation

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True  # This allows the model to work with SQLAlchemy objects