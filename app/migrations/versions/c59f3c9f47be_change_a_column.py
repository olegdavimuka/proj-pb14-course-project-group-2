"""Change a column

Revision ID: c59f3c9f47be
Revises: a69a0da29cc0
Create Date: 2023-12-11 10:28:10.664941

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "c59f3c9f47be"
down_revision: Union[str, None] = "a69a0da29cc0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Remove the column "avatar"
    op.drop_column("users", "avatar")
    # Add the new column "occupation"
    op.add_column("users", sa.Column("occupation", sa.String))


def downgrade() -> None:
    # Remove the new column "occupation"
    op.drop_column("users", "occupation")
    # Add the removed column "avatar" back
    op.add_column("users", sa.Column("avatar", sa.String))
