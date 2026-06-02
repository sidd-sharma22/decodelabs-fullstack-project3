from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

# User Schemas

## Request body (create user)
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr

## Response body
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# Task Schemas

## Request body
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    status: Optional[str] = "Pending"
    user_id: int

## Response body
class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    user_id: int

    class Config:
        from_attributes = True

class TaskMini(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        from_attributes = True


## Nested Task List
class UserWithTasks(BaseModel):
    id: int
    name: str
    email: str
    tasks: List[TaskMini] = []

    class Config:
        from_attributes = True