from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

class MongoDBManager:
    """
    MongoDB 커넥션 관리 클래스
    """
    client: Optional[AsyncIOMotorClient] = None

    def connect_to_database(self, db_url: str):
        self.client = AsyncIOMotorClient(db_url)
        print("MongoDB connected")

    def close_database_connection(self):
        if self.client:
            self.client.close()
            print("MongoDB disconnected")

db_manager = MongoDBManager()