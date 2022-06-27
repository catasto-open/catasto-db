"""Added ctcn.cutipnot

Revision ID: 2dd333f65ddc
Revises: c6a95d68540a
Create Date: 2022-06-07 16:54:35.147579

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "2dd333f65ddc"
down_revision = "c6a95d68540a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cutipnot",
        sa.Column("tipo_nota", sa.String(length=1), nullable=False),
        sa.Column("descrizion", sa.String(length=35), nullable=False),
        sa.PrimaryKeyConstraint("tipo_nota", name="cutipnot_pkey"),
        schema="ctcn",
    )


def downgrade() -> None:
    op.drop_table("cutipnot", schema="ctcn")
