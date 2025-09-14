from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends

from app.dependencies import get_my_service
from app.schemas.todo import TodoModel
from app.schemas.todo_update import TodoUpdateModel
from app.services.todo_service import TodoService
from typing import List, Optional

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)

@router.get("/", response_model=List[TodoModel], status_code=status.HTTP_200_OK)
async def get_todos(todo_service: TodoService = Depends(get_my_service)) -> List[TodoModel]:
    todos = await todo_service.get_todos()
    return todos

@router.get("/{todo_id}", response_model=TodoModel, status_code=status.HTTP_200_OK)
async def get_todo(todo_id: str, todo_service: TodoService = Depends(get_my_service)) -> Optional[TodoModel]:
    todo = await todo_service.get_todo(todo_id)

    return todo

@router.post("/", status_code=status.HTTP_201_CREATED)
async def insert_todo(todo_input: TodoModel, todo_service: TodoService = Depends(get_my_service)) -> bool:
    await todo_service.create_todo(todo_input)
    return True

@router.patch("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo_input: TodoUpdateModel, todo_id: str, todo_service: TodoService = Depends(get_my_service)):
    await todo_service.update_todo(todo_id, todo_input)