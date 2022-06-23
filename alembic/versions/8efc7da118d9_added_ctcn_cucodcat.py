"""Added ctcn.cucodcat

Revision ID: 8efc7da118d9
Revises: 1bd9c920a51a
Create Date: 2022-06-07 16:21:11.933000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8efc7da118d9"
down_revision = "1bd9c920a51a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cucodcat",
        sa.Column("categoria", sa.String(length=3), nullable=False),
        sa.Column("descrizion", sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint("categoria", name="cucodcat_pkey"),
        schema="ctcn",
    )


def downgrade() -> None:
    op.drop_table("cucodcat", schema="ctcn")
