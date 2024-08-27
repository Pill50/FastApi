from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from share.database import get_db_context
import services.user as userService
from models.user import UserViewModel

router = APIRouter(prefix="/users", tags=["User"])


@router.get("", response_model=list[UserViewModel])
async def get_users(db: Session = Depends(get_db_context)) -> list[UserViewModel]:
    return userService.get_users(db)


@router.get("/{user_id}", response_model=UserViewModel)
async def get_user_by_id(
    user_id: str, db: Session = Depends(get_db_context)
) -> UserViewModel:
    return userService.get_user_by_id(user_id, db)
