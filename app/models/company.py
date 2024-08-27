from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from schemas.task import TaskPriority, TaskStatus
from schemas.company import CompanyMode


class CompanyViewModel(BaseModel):
    id: UUID
    name: str
    description: str
    mode: CompanyMode
    rating: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CompanyTaskViewModel(BaseModel):
    id: UUID
    summary: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
