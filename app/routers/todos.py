from fastapi import APIRouter, status, Request
from fastapi.params import Depends

from app.dependencies import get_my_service
from app.schemas.todo import TodoModel
from app.services.todo_service import TodoService
from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection
from app.database import db_manager

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)

@router.get("/", response_model=List[TodoModel], status_code=status.HTTP_200_OK)
async def get_todos(todo_service: TodoService = Depends(get_my_service)) -> List[TodoModel]:
    todos = await todo_service.get_todos()
    print(todos)
    return todos