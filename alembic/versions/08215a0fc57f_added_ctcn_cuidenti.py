"""Added ctcn.cuidenti

Revision ID: 08215a0fc57f
Revises: c7e260c04a48
Create Date: 2022-06-07 16:33:04.291062

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "08215a0fc57f"
down_revision = "c7e260c04a48"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cuidenti",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("sezione", sa.String(length=1), nullable=False),
        sa.Column("immobile", sa.BigInteger(), nullable=False),
        sa.Column("tipo_imm", sa.String(length=1), nullable=False),
        sa.Column("progressiv", sa.Integer(), nullable=False),
        sa.Column("sez_urbana", sa.String(length=3), nullable=True),
        sa.Column("foglio", sa.String(length=4), nullable=True),
        sa.Column("numero", sa.String(length=5), nullable=True),
        sa.Column("denominato", sa.Integer(), nullable=True),
        sa.Column("subalterno", sa.String(length=4), nullable=True),
        sa.Column("edificiale", sa.String(length=1), nullable=True),
        schema="ctcn",
    )
    op.create_index(
        "cuidenti_idx1",
        "cuidenti",
        ["codice", "sezione", "immobile", "tipo_imm", "progressiv"],
        schema="ctcn",
        postgresql_using="btree",
    )
    op.create_index(
        "cuidenti_idx2",
        "cuidenti",
        ["codice", "sezione", "foglio", "numero"],
        schema="ctcn",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "cuidenti_idx1",
        table_name="cuidenti",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_index(
        "cuidenti_idx2",
        table_name="cuidenti",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_table("cuidenti", schema="ctcn")
