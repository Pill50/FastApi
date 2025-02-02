from fastapi import APIRouter, status, Depends
from models.user import CreateUserDto
from services.user import create_user
import services.auth as auth_service
from fastapi.security import OAuth2PasswordRequestForm
from share.database import get_db_context
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(dto: CreateUserDto, db: Session = Depends(get_db_context)):
    return create_user(dto, db)


@router.post("/login")
async def login(
    dto: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_context)
):
    return auth_service.login(dto, db)
