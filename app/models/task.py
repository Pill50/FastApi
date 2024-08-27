from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

from schemas.task import TaskPriority, TaskStatus


class TaskViewModel(BaseModel):
    id: UUID
    summary: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreateTaskDto(BaseModel):
    summary: str = Field(min_length=3)
    description: str = Field()
    status: TaskStatus = Field(default=TaskStatus.OPEN)
    priority: TaskPriority = Field(default=TaskPriority.LOW)


class UpdateTaskDto(BaseModel):
    summary: str = Field(min_length=3)
    description: str = Field()
