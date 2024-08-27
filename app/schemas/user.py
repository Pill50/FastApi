from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from share.database import Base
from schemas.base_entity import BaseEntity
from sqlalchemy.orm import relationship


class User(Base, BaseEntity):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="user", uselist=False)

    tasks = relationship("Task", back_populates="user")
