"""Added ctmp schema

Revision ID: cc51b80407c6
Revises: 1f81a8a100e8
Create Date: 2022-06-07 17:56:22.450979

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'cc51b80407c6'
down_revision = '1f81a8a100e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("create schema ctmp")


def downgrade() -> None:
    op.execute("drop schema ctmp")

