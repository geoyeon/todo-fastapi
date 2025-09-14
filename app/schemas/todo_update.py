from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoUpdateModel(BaseModel):
    title: Optional[str] = None

    memo: Optional[str] = None

    startDate: Optional[datetime] = None

    endDate: Optional[datetime] = None

    isComplete: Optional[bool] = None

    updatedAt: datetime = datetime.now()

    model_config = {
        'populate_by_name': True
    }
