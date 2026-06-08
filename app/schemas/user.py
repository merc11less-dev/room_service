from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime


class UserRole(str, Enum):
    employee = 'employee'
    admin = 'admin'


class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole = UserRole.employee


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True