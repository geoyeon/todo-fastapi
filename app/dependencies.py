from fastapi import Request, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from services.todo_service import TodoService

def get_db(request: Request) -> AsyncIOMotorDatabase:
    return request.app.mongodb

def get_my_service(db: AsyncIOMotorDatabase = Depends(get_db)) -> TodoService:
    return TodoService(db)