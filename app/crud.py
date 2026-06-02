from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas

# User CRUD

## Create User
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email
    )

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    except IntegrityError:
        db.rollback()
        return None


## Get All Users
def get_users(db: Session):
    return db.query(models.User).all()


## Get Single User
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


# Task CRUD

## Create Task
def create_task(db: Session, task: schemas.TaskCreate):
    user = db.query(models.User).filter(
        models.User.id == task.user_id
    ).first()

    if not user:
        return None

    db_task = models.Task(
        title=task.title,
        status=task.status,
        user_id=task.user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


## Get All Tasks
def get_tasks(db: Session):
    return db.query(models.Task).all()


## Get Single Task
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()


## Update Task
def update_task(db: Session, task_id: int, task: schemas.TaskCreate):
    db_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if db_task:
        db_task.title = task.title
        if task.status is not None:
            db_task.status = task.status
        db_task.user_id = task.user_id

        db.commit()
        db.refresh(db_task)

    return db_task


## Delete Task
def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if db_task:
        db.delete(db_task)
        db.commit()

    return db_task

# Relationship Queries

## Get a user's tasks
def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(
        models.Task.user_id == user_id
    ).all()


## Get user with tasks
def get_user_with_tasks(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()