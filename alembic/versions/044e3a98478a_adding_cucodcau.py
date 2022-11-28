"""Adding ctcn cucodcau

Revision ID: 044e3a98478a
Revises: 4efc3b267ac9
Create Date: 2022-11-17 15:47:30.743180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '044e3a98478a'
down_revision = '4efc3b267ac9'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table(
        "cucodcau",
        sa.Column("cod_causa", sa.String(length=3), nullable=False),
        sa.Column("descrizion", sa.String(length=65), nullable=False),
        sa.PrimaryKeyConstraint("cod_causa", name="cucodcau_pkey"),
        schema="ctcn",
    )

def downgrade() -> None:
    op.drop_table("cucodcau", schema="ctcn")
