"""Added ctcn.cttitola

Revision ID: eeab6e618666
Revises: 228fb2ce24d3
Create Date: 2022-06-07 15:38:29.001979

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "eeab6e618666"
down_revision = "228fb2ce24d3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cttitola",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("sezione", sa.String(length=1), nullable=False),
        sa.Column("soggetto", sa.BigInteger(), nullable=False),
        sa.Column("tipo_sog", sa.String(length=1), nullable=False),
        sa.Column("immobile", sa.BigInteger(), nullable=False),
        sa.Column("tipo_imm", sa.String(length=1), nullable=False),
        sa.Column("diritto", sa.String(length=3), nullable=True),
        sa.Column("titolo", sa.String(length=200), nullable=True),
        sa.Column("numeratore", sa.Integer(), nullable=True),
        sa.Column("denominato", sa.Integer(), nullable=True),
        sa.Column("regime", sa.String(length=1), nullable=True),
        sa.Column("rif_regime", sa.Integer(), nullable=True),
        sa.Column("gen_valida", sa.String(length=10), nullable=True),
        sa.Column("gen_nota", sa.String(length=1), nullable=True),
        sa.Column("gen_numero", sa.String(length=6), nullable=True),
        sa.Column("gen_progre", sa.String(length=3), nullable=True),
        sa.Column("gen_anno", sa.String(length=4), nullable=True),
        sa.Column("gen_regist", sa.String(length=10), nullable=True),
        sa.Column("partita", sa.String(length=7), nullable=True),
        sa.Column("con_valida", sa.String(length=10), nullable=True),
        sa.Column("con_nota", sa.String(length=1), nullable=True),
        sa.Column("con_numero", sa.String(length=6), nullable=True),
        sa.Column("con_progre", sa.String(length=3), nullable=True),
        sa.Column("con_anno", sa.String(length=4), nullable=True),
        sa.Column("con_regist", sa.String(length=10), nullable=True),
        sa.Column("mutaz_iniz", sa.Integer(), nullable=True),
        sa.Column("mutaz_fine", sa.Integer(), nullable=True),
        sa.Column("identifica", sa.Integer(), nullable=False),
        sa.Column("gen_causa", sa.String(length=3), nullable=True),
        sa.Column("gen_descr", sa.String(length=100), nullable=True),
        sa.Column("con_causa", sa.String(length=3), nullable=True),
        sa.Column("con_descr", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint(
            "codice", "sezione", "identifica", name="cttitola_pkey"
        ),
        schema="ctcn",
    )
    op.create_index(
        "cttitola_idx1",
        "cttitola",
        ["codice", "sezione", "soggetto", "tipo_sog"],
        schema="ctcn",
        postgresql_using="btree",
    )
    op.create_index(
        "cttitola_idx2",
        "cttitola",
        ["codice", "sezione", "immobile", "tipo_imm"],
        schema="ctcn",
        postgresql_using="btree",
    )
    op.create_index(
        "cttitola_soggetto_idx",
        "cttitola",
        ["soggetto", "tipo_sog"],
        schema="ctcn",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "cttitola_idx1",
        table_name="cttitola",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_index(
        "cttitola_idx2",
        table_name="cttitola",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_index(
        "cttitola_soggetto_idx",
        table_name="cttitola",
        schema="ctcn",
        postgresql_using="btree",
    )
    op.drop_table("cttitola", schema="ctcn")
