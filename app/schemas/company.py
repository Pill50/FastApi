import enum

from sqlalchemy import Column, Enum, Numeric, String
from sqlalchemy.orm import relationship
from share.database import Base
from schemas.base_entity import BaseEntity


class CompanyMode(enum.Enum):
    PUBLIC = "public"
    PRIVATE = "private"


class Company(Base, BaseEntity):
    __tablename__ = "companies"

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    mode = Column(Enum(CompanyMode), default=CompanyMode.PRIVATE, nullable=False)
    rating = Column(Numeric, nullable=True)

    user = relationship("User", back_populates="company", uselist=False)
