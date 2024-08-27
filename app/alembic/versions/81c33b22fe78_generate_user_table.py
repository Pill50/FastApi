"""generate user table

Revision ID: 81c33b22fe78
Revises: 
Create Date: 2024-08-21 09:28:35.106949

"""

from datetime import datetime
from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa

from share.settings import DEFAULT_PASSWORD
from services.user import get_hash_password


# revision identifiers, used by Alembic.
revision: str = "81c33b22fe78"
down_revision: Union[str, None] = "647be04a6025"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # User Table
    user_table = op.create_table(
        "users",
        sa.Column("id", sa.UUID, primary_key=True),
        sa.Column("first_name", sa.String, nullable=False),
        sa.Column("last_name", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("username", sa.String, nullable=False, unique=True),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False, default=True),
        sa.Column("is_admin", sa.Boolean, nullable=False, default=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        sa.Column("company_id", sa.UUID, sa.ForeignKey("companies.id"), nullable=True),
    )
    op.create_index("idx_usr_fst_lst_name", "users", ["first_name", "last_name"])
    op.create_index("idx_users_username", "users", ["username"])
    op.create_index("idx_users_frt_las_name", "users", ["first_name", "last_name"])

    # Data seed for first user
    op.bulk_insert(
        user_table,
        [
            {
                "id": uuid4(),
                "email": "user@gmail.com",
                "username": "user",
                "hashed_password": get_hash_password(DEFAULT_PASSWORD),
                "first_name": "FastApi",
                "last_name": "User",
                "is_active": True,
                "is_admin": True,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
                "company_id": "1161dbf0-132e-4f89-a121-c5e9ebba48ec",
            },
            {
                "id": uuid4(),
                "email": "admin@gmail.com",
                "username": "admin",
                "hashed_password": get_hash_password(DEFAULT_PASSWORD),
                "first_name": "FastApi",
                "last_name": "Admin",
                "is_active": True,
                "is_admin": True,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
                "company_id": "0c5300ee-3b42-4e9e-8a4c-08626de7a889",
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("users")
