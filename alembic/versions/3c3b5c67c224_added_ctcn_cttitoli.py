"""Added ctcn.cttitoli

Revision ID: 3c3b5c67c224
Revises: eeab6e618666
Create Date: 2022-06-07 15:47:10.353112

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "3c3b5c67c224"
down_revision = "eeab6e618666"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cttitoli",
        sa.Column("codice", sa.String(length=3), nullable=False),
        sa.Column("titolo", sa.String(length=53), nullable=False),
        sa.PrimaryKeyConstraint("codice", name="cttitoli_pkey"),
        schema="ctcn",
    )


def downgrade() -> None:
    op.drop_table("cttitoli", schema="ctcn")
