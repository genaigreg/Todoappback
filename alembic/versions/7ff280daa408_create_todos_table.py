"""create todos table

Revision ID: 7ff280daa408
Revises: ad1c380734f8
Create Date: 2024-09-11 15:04:51.904842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ff280daa408'
down_revision: Union[str, None] = 'ad1c380734f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    create table putos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)


def downgrade() -> None:
    pass
