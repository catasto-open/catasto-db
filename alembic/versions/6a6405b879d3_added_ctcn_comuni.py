"""Added ctcn.comuni

Revision ID: 6a6405b879d3
Revises: fa5b6e5e49d9
Create Date: 2022-06-07 12:08:36.475774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6a6405b879d3"
down_revision = "fa5b6e5e49d9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "comuni",
        sa.Column("provincia", sa.String(length=2), nullable=False),
        sa.Column("comune", sa.String(length=65), nullable=False),
        sa.Column("codice", sa.String(length=5), nullable=False),
        sa.PrimaryKeyConstraint("codice", name="comuni_pkey"),
        schema="ctcn",
    )


def downgrade() -> None:
    op.drop_table("comuni", schema="ctcn")
