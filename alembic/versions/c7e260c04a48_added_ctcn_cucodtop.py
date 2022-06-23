"""Added ctcn.cucodtop

Revision ID: c7e260c04a48
Revises: 8efc7da118d9
Create Date: 2022-06-07 16:22:31.759561

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "c7e260c04a48"
down_revision = "8efc7da118d9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cucodtop",
        sa.Column("codice", sa.Integer(), nullable=False, autoincrement=False),
        sa.Column("toponimo", sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint("codice", name="cucodtop_pkey"),
        schema="ctcn",
    )


def downgrade() -> None:
    op.drop_table("cucodtop", schema="ctcn")
