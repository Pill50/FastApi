import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from share.database import Base
from schemas.base_entity import BaseEntity


class TaskPriority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStatus(enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(Base, BaseEntity):
    __tablename__ = "tasks"

    summary = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(Enum(TaskPriority), default=TaskPriority.LOW, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.OPEN, nullable=False)

    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="tasks")
