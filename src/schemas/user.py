from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0)


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: Optional[int]

    class Config:
        orm_mode = True
