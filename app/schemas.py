from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

# User schemas

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


# Fitness class schemas

class ClassCreate(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    available_slots: int


class ClassResponse(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True

    
# Booking schemas

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr