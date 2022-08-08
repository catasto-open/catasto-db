"""added ctcn comuni_

Revision ID: 3fc7bd349450
Revises: e73f038c81f4
Create Date: 2022-08-03 16:57:05.983157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc7bd349450'
down_revision = 'e73f038c81f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "comuni_",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("provincia", sa.String(length=2), nullable=False),
        sa.Column("comune", sa.String(length=1000), nullable=False),
        sa.Column("comune_straniero", sa.String(length=1000),nullable=True),
        sa.Column("codice_catastale", sa.String(length=5),nullable=True),
        sa.Column("ufficio_terreni", sa.String(length=2),nullable=True),
        sa.Column("conservatoria", sa.String(length=5), nullable=True),
        sa.Column("istat", sa.String(length=10),nullable=True),
        sa.Column("data_inizio", sa.Date(), nullable=True),
        sa.Column("data_variazione", sa.Date(), nullable=True),
        sa.Column("tipo", sa.String(length=1),nullable=True),
        schema="ctcn"
    )

    op.create_index(
        "comuni__index01",
        "comuni_",
        ["codice", "provincia", "comune", "data_inizio", "data_variazione"],
        schema="ctcn",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "comuni__index01",
        table_name="comuni_",
        schema="ctcn",
        postgresql_using="btree"
    )
    op.drop_table(
        "comuni_", schema="ctcn"
    )

