"""added ctcn sezioni_

Revision ID: 1982aabfb5e9
Revises: 3fc7bd349450
Create Date: 2022-08-03 16:58:42.955680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1982aabfb5e9'
down_revision = '3fc7bd349450'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "sezioni_",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("sezione", sa.String(length=1), nullable=False),
        sa.Column("comune", sa.String(length=1000), nullable=False),
        sa.Column("catasto", sa.String(1), nullable=False),
        sa.Column("stato", sa.String(length=1000), nullable=False),
        schema="ctcn"
    )


def downgrade() -> None:
    op.drop_table(
        "sezioni_", schema="ctcn"
    )

