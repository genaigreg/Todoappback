"""create todos table

Revision ID: 7a41cf62edc4
Revises: 7ff280daa408
Create Date: 2024-09-11 15:09:26.268094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a41cf62edc4'
down_revision: Union[str, None] = '7ff280daa408'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
