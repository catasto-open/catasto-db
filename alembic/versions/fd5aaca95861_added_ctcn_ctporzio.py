"""Added ctcn.ctporzio

Revision ID: fd5aaca95861
Revises: 2aa6b7a59a8e
Create Date: 2022-06-07 14:41:26.485282

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "fd5aaca95861"
down_revision = "2aa6b7a59a8e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ctporzio",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("sezione", sa.String(length=1), nullable=False),
        sa.Column("immobile", sa.BigInteger(), nullable=False),
        sa.Column("tipo_imm", sa.String(length=1), nullable=False),
        sa.Column("progressiv", sa.Integer(), nullable=False),
        sa.Column("porzione", sa.String(length=2), nullable=True),
        sa.Column("qualita", sa.Integer(), nullable=True),
        sa.Column("classe", sa.String(length=2), nullable=True),
        sa.Column("ettari", sa.Integer(), nullable=True),
        sa.Column("are", sa.Integer(), nullable=True),
        sa.Column("centiare", sa.Integer(), nullable=True),
        sa.Column("dominic_e", sa.String(length=12), nullable=True),
        sa.Column("agrario_e", sa.String(length=11), nullable=True),
        schema="ctcn",
    )
    op.create_index(
        "ctporzio_idx1",
        "ctporzio",
        ["codice", "sezione", "immobile", "tipo_imm", "progressiv"],
        schema="ctcn",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "ctporzio_idx1",
        table_name="ctporzio",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_table("ctporzio", schema="ctcn")
