"""Add a column

Revision ID: a69a0da29cc0
Revises: c65392f24428
Create Date: 2023-12-10 20:36:05.243808

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "a69a0da29cc0"
down_revision: Union[str, None] = "c65392f24428"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("users", "age", type_=sa.String)


def downgrade() -> None:
    op.alter_column("users", "age", type_=sa.Integer)
