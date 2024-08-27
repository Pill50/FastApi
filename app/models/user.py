from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

from models.company import CompanyViewModel


class CreateUserDto(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr = Field()
    password: str = Field(min_length=3)
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)


class UserViewModel(BaseModel):
    id: UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_admin: bool
    created_at: datetime
    updated_at: datetime
    company: Optional[CompanyViewModel] = None

    class Config:
        from_attributes = True
