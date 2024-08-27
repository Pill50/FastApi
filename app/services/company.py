from sqlalchemy.orm import Session

from schemas.user import User
from schemas.company import Company


def get_companies(db: Session) -> list[Company]:
    return db.query(Company).all()


def get_users_company(company_id: str, db: Session):
    return db.query(User).filter(User.company_id == company_id).all()
