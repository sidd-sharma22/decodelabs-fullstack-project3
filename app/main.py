from fastapi import FastAPI

from app.database import engine
from app import models
from app.routes import router

# Create Tables
models.Base.metadata.create_all(bind=engine)

# Swagger Description
app = FastAPI(
    title="StudyHub API",
    description="Task management backend using FastAPI + PostgreSQL",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "StudyHub API is Running"}