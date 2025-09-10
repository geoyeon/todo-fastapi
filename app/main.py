# app/main.py
import os
from typing import Optional

from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import db_manager
from environment import environments
from app import routers


MONGO_DB_URL = environments.mongo_db_uri
MONGO_DB_NAME = environments.mongo_db_name

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    db_manager.connect_to_database(MONGO_DB_URL)
    app.mongodb = db_manager.client[MONGO_DB_NAME]
    yield
    db_manager.close_database_connection()

app = FastAPI(
    title="Todo FastAPI",
    description="Todo FastAPI",
    version="0.1.0",
    lifespan=db_lifespan
)

app.include_router(routers.todos.router)

@app.get("/")
async def root():
    return {"message": "Hello Todo"}

@app.get("/items/{item_id}")
async def get_todo(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
