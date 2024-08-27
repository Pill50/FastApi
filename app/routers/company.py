from fastapi import APIRouter, Depends
from share.database import get_db_context
from models.user import UserViewModel
from models.company import CompanyTaskViewModel, CompanyViewModel
import services.company as service
from services.auth import authenticate, get_user, admin_guard
from schemas.user import User
from common.error import NotFoundException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("", response_model=list[CompanyViewModel])
async def get_companies():
    return service.get_companies()


@router.get(
    "/me", response_model=CompanyViewModel, dependencies=[Depends(authenticate)]
)
async def get_own_company(user: User = Depends(get_user)):
    if user.company is None:
        raise NotFoundException()
    return user.company


@router.get(
    "/user", response_model=list[UserViewModel], dependencies=[Depends(authenticate)]
)
async def get_usera_company(
    user: User = Depends(get_user), db: Session = Depends(get_db_context)
):
    if user.company is None:
        raise NotFoundException()
    return service.get_users_company(user.company_id, db)


@router.get(
    "/task",
    response_model=list[CompanyTaskViewModel],
    dependencies=[Depends(authenticate), Depends(admin_guard)],
)
async def get_company_tasks(
    user: User = Depends(get_user), db: Session = Depends(get_db_context)
):
    return service.get_company_tasks(user.company_id, db)
