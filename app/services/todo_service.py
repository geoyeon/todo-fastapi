from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo import DESCENDING

from app.schemas.todo import TodoModel

import logging

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
