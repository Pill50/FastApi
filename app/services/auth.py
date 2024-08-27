from common.error import (
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
)
from share.database import get_db_context
from share.settings import JWT_REFRESH_SECRET, JWT_SECRET, JWT_ALGORITHM
from schemas.user import User
from .user import verify_password, get_user_by_id
from datetime import timedelta, datetime
from fastapi import Request, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def login(dto: OAuth2PasswordRequestForm, db: Session):
    user = db.query(User).filter(User.username == dto.username).first()

    if not user:
        raise BadRequestException()

    if not verify_password(dto.password, user.hashed_password):
        raise BadRequestException()

    access_token = create_jwt(user, JWT_SECRET, JWT_ALGORITHM, timedelta(hours=1))
    refresh_token = create_jwt(
        user, JWT_REFRESH_SECRET, JWT_ALGORITHM, timedelta(days=1)
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def create_jwt(user: User, secret: str, algorithm: str, expires: timedelta = None):
    payload = {
        "id": str(user.id),
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_active": user.is_active,
        "is_admin": user.is_admin,
    }
    expire = (
        datetime.now() + expires if expires else datetime.now() + timedelta(minutes=10)
    )
    payload.update({"exp": expire})
    return jwt.encode(payload, secret, algorithm=algorithm)


def verify_jwt(token: str, secret: str, algorithm: str):
    return jwt.decode(token, secret, algorithms=[algorithm])


def refresh_token(token: str):
    try:
        payload = verify_jwt(token, JWT_REFRESH_SECRET, JWT_ALGORITHM)
        access_token = create_jwt(
            User(**payload), JWT_SECRET, JWT_ALGORITHM, timedelta(minutes=10)
        )
        return {"access_token": access_token}
    except Exception:
        raise BadRequestException()


def authenticate(
    request: Request,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db_context),
):
    try:
        payload = verify_jwt(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        user = get_user_by_id(payload["id"], db)

        if not user.is_active:
            raise UnauthorizedException()

        request.state.user = user
    except Exception as e:
        print(e)
        raise UnauthorizedException()


def admin_guard(request: Request):
    user = request.state.user

    if user.company is None:
        raise ForbiddenException()

    if not user.is_admin:
        raise ForbiddenException()


def get_user(request: Request):
    return request.state.user
