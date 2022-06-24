"""Added ctcn.ctcodris

Revision ID: 0b3dc6b9ed65
Revises: 6a6405b879d3
Create Date: 2022-06-07 13:22:06.324936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0b3dc6b9ed65"
down_revision = "6a6405b879d3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ctcodris",
        sa.Column("codice", sa.String(length=1), nullable=False),
        sa.Column("descrizion", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("codice", name="ctcodris_pkey"),
        schema="ctcn",
    )


def downgrade() -> None:
    op.drop_table("ctcodris", schema="ctcn")
