from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


# User Routes

## Create a user
@router.post("/users", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(db, user)

    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    return new_user


## Get all user
@router.get("/users", response_model=list[schemas.UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


## Get a user
@router.get("/users/{user_id}", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


## Get all tasks assigned to user
@router.get("/users/{user_id}/tasks", response_model=list[schemas.TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks_by_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return crud.get_tasks_by_user(db, user_id)


## Get all users assigned with task
@router.get("/users/{user_id}/full", response_model=schemas.UserWithTasks, status_code=status.HTTP_200_OK)
def get_user_with_tasks(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_with_tasks(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


# Task Routes

## Create a Task
@router.post("/tasks", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = crud.create_task(db, task)

    if not new_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return new_task



## Get All Tasks
@router.get("/tasks", response_model=list[schemas.TaskResponse], status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


## Get One Task
@router.get("/tasks/{task_id}", response_model=schemas.TaskResponse, status_code=status.HTTP_200_OK)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


## Update Task
@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse, status_code=status.HTTP_202_ACCEPTED)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)

    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return updated_task


## Delete Task
@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}