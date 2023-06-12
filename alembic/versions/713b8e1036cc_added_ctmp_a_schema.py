"""Added ctmp_a schema

Revision ID: 713b8e1036cc
Revises: dfab1acceab5
Create Date: 2022-06-08 08:34:08.301077

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "713b8e1036cc"
down_revision = "dfab1acceab5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("create schema ctmp_a")


def downgrade() -> None:
    op.execute("drop schema ctmp_a")
