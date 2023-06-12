"""Adding ctcn version

Revision ID: 347ca562f469
Revises: 044e3a98478a
Create Date: 2022-11-17 16:00:10.878773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '347ca562f469'
down_revision = '044e3a98478a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "version",
        sa.Column("codice", sa.String(length=64), nullable=False),
        sa.Column("data_aggiornamento", sa.Date, nullable=False),
        sa.PrimaryKeyConstraint("codice", name="version_pkey"),
        schema="ctcn",
    )


def downgrade() -> None:
    op.drop_table("version", schema="ctcn")
