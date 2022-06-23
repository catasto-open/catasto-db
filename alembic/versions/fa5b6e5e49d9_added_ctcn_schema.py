"""Added ctcn schema

Revision ID: fa5b6e5e49d9
Revises: 6157bae19f10
Create Date: 2022-06-07 12:04:44.769309

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "fa5b6e5e49d9"
down_revision = "6157bae19f10"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("create schema ctcn")


def downgrade() -> None:
    op.execute("drop schema ctcn")
