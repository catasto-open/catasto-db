"""Added ctcn.ctfisica

Revision ID: 5899db015043
Revises: 7b042ea61bc2
Create Date: 2022-06-07 13:55:09.357798

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = "5899db015043"
down_revision = "7b042ea61bc2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ctfisica",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("sezione", sa.String(length=1), nullable=False),
        sa.Column("soggetto", sa.BigInteger(), nullable=False),
        sa.Column("tipo_sog", sa.String(length=1), nullable=False),
        sa.Column("cognome", sa.String(length=50), nullable=True),
        sa.Column("nome", sa.String(length=50), nullable=True),
        sa.Column("sesso", sa.String(length=1), nullable=True),
        sa.Column("data", sa.String(length=10), nullable=True),
        sa.Column("luogo", sa.String(length=4), nullable=True),
        sa.Column("codfiscale", sa.String(length=16), nullable=True),
        sa.Column("supplement", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint(
            "codice", "sezione", "soggetto", "tipo_sog", name="ctfisica_pkey"
        ),
        schema="ctcn",
    )
    op.create_index(
        "ctfisica_i1",
        "ctfisica",
        [
            text("cognome varchar_pattern_ops"),
            text("nome varchar_pattern_ops"),
        ],
        schema="ctcn",
        postgresql_using="btree",
    )
    op.create_index(
        "ctfisica_i2",
        "ctfisica",
        [text("codfiscale varchar_pattern_ops")],
        schema="ctcn",
        postgresql_using="btree",
    )
    op.create_index(
        "ctfisica_i3",
        "ctfisica",
        [
            text(
                "((((cognome)::text || ' '::text) || (nome)::text)) varchar_pattern_ops"
            )
        ],
        schema="ctcn",
        postgresql_using="btree",
    )
    op.create_index(
        "ctfisica_index01",
        "ctfisica",
        ["luogo"],
        schema="ctcn",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "ctfisica_i1",
        table_name="ctfisica",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_index(
        "ctfisica_i2",
        table_name="ctfisica",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_index(
        "ctfisica_i3",
        table_name="ctfisica",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_index(
        "ctfisica_index01",
        table_name="ctfisica",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_table("ctfisica", schema="ctcn")
