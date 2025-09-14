from typing import List, Optional

from bson import ObjectId
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo import DESCENDING
from pymongo.results import InsertOneResult, UpdateResult

from app.schemas.todo import TodoModel

import logging

from app.schemas.todo_update import TodoUpdateModel

logging.basicConfig(level=logging.INFO)
logging.getLogger("motor").setLevel(logging.DEBUG)

class TodoService:
    """
    Todo 서비스 클래스
    """
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    async def get_todos(self) -> List[TodoModel]:
        """
        모든 Todo를 가져옵니다.
        :return:
        """
        todos = await self.db.todos.find().sort(key_or_list='_id', direction=DESCENDING).to_list()
        return [TodoModel(**todo) for todo in todos]

    async def get_todo(self, todo_id: str) -> Optional[TodoModel]:
        """
        특정 Todo를 가져옵니다.
        """
        try:
            todo_object_id = ObjectId(todo_id)
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Todo ID",
            )

        todo = await self.db.todos.find_one({"_id": todo_object_id})
        print(todo)

        if todo:
            return TodoModel(**todo)
        return None

    async def create_todo(self, input_todo: TodoModel) -> InsertOneResult:
        """
        새로운 Todo를 생성합니다.
        """
        input_data = input_todo.model_dump(by_alias=True, exclude_none=True)
        print(input_data)
        result = await self.db.todos.insert_one(input_data)
        print(result)
        return result

    async def update_todo(self, todo_id: str, update_todo: TodoUpdateModel) -> UpdateResult:
        """
        특정 Todo를 업데이트합니다.
        """
        try:
            todo_object_id = ObjectId(todo_id)
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Todo ID",
            )

        update_data = update_todo.model_dump(by_alias=True, exclude_none=True)

        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No data to update",
            )

        result = await self.db.todos.update_one({"_id": todo_object_id}, {"$set": update_data })

        return result
        # return True