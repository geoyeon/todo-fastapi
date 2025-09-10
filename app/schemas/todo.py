from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.pyobjectid import PyObjectId
class TodoModel(BaseModel):
    id: Optional[PyObjectId] = Field(None, alias="_id")

    title: str

    memo: Optional[str] = None

    startDate: datetime

    endDate: datetime

    isComplete: Optional[bool] = False

    createdAt: Optional[datetime] = None

    updatedAt: Optional[datetime] = None

    model_config = {
        'populate_by_name': True
    }
