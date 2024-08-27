from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, Time, Uuid


class BaseEntity:
    id = Column(Uuid, primary_key=True, default=uuid4)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
