"""Added ctcn.cuindiri

Revision ID: a843bb3ee075
Revises: 08215a0fc57f
Create Date: 2022-06-07 16:42:54.004532

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "a843bb3ee075"
down_revision = "08215a0fc57f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cuindiri",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("sezione", sa.String(length=1), nullable=False),
        sa.Column("immobile", sa.BigInteger(), nullable=False),
        sa.Column("tipo_imm", sa.String(length=1), nullable=False),
        sa.Column("progressiv", sa.Integer(), nullable=False),
        sa.Column("toponimo", sa.Integer(), nullable=True),
        sa.Column("indirizzo", sa.String(length=50), nullable=True),
        sa.Column("civico1", sa.String(length=6), nullable=True),
        sa.Column("civico2", sa.String(length=6), nullable=True),
        sa.Column("civico3", sa.String(length=6), nullable=True),
        sa.Column("cod_strada", sa.String(length=5), nullable=True),
        schema="ctcn",
    )
    op.create_index(
        "cuindiri_idx1",
        "cuindiri",
        ["codice", "sezione", "immobile", "tipo_imm", "progressiv"],
        schema="ctcn",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "cuindiri_idx1",
        table_name="cuindiri",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_table("cuindiri", schema="ctcn")
