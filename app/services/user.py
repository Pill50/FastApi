from uuid import UUID
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from schemas.user import User
from common.error import BadRequestException
from models.user import CreateUserDto

bcrypt_context = CryptContext(schemes=["bcrypt"])


def get_hash_password(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hased_password):
    return bcrypt_context.verify(plain_password, hased_password)


def get_users(db: Session) -> list[User]:
    return db.query(User).filter(User.is_active == True).all()


def get_user_by_id(user_id: UUID, db: Session) -> User:
    user = db.query(User).filter(User.id == user_id).one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def create_user(dto: CreateUserDto, db: Session):
    exist_user = (
        db.query(User).filter(User.email == dto.email).first()
        or db.query(User).filter(User.username == dto.username).first()
    )

    if exist_user:
        raise BadRequestException()

    params = dto.model_dump()

    params["hashed_password"] = get_hash_password(params["password"])
    del params["password"]

    user = User(**params)
    db.add(user)
    db.commit()
