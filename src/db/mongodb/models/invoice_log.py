from datetime import datetime
from typing import List
from pydantic import BaseModel


class Change(BaseModel):
    field: str
    old_value: str
    new_value: str


class InvoiceLog(BaseModel):
    user_id: int
    date: datetime
    changes: List[Change]
