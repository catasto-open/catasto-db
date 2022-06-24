"""Added ctcn.cuarcuiu

Revision ID: 1bd9c920a51a
Revises: 3c3b5c67c224
Create Date: 2022-06-07 15:52:33.064513

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "1bd9c920a51a"
down_revision = "3c3b5c67c224"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cuarcuiu",
        sa.Column("codice", sa.String(length=4), nullable=False),
        sa.Column("sezione", sa.String(length=1), nullable=False),
        sa.Column("immobile", sa.BigInteger(), nullable=False),
        sa.Column("tipo_imm", sa.String(length=1), nullable=False),
        sa.Column("progressiv", sa.Integer(), nullable=False),
        sa.Column("zona", sa.String(length=3), nullable=True),
        sa.Column("categoria", sa.String(length=3), nullable=True),
        sa.Column("classe", sa.String(length=2), nullable=True),
        sa.Column("consistenz", sa.String(length=7), nullable=True),
        sa.Column("superficie", sa.String(length=5), nullable=True),
        sa.Column("rendita_l", sa.String(length=15), nullable=True),
        sa.Column("rendita_e", sa.String(length=18), nullable=True),
        sa.Column("lotto", sa.String(length=2), nullable=True),
        sa.Column("edificio", sa.String(length=2), nullable=True),
        sa.Column("scala", sa.String(length=2), nullable=True),
        sa.Column("interno_1", sa.String(length=3), nullable=True),
        sa.Column("interno_2", sa.String(length=3), nullable=True),
        sa.Column("piano_1", sa.String(length=4), nullable=True),
        sa.Column("piano_2", sa.String(length=4), nullable=True),
        sa.Column("piano_3", sa.String(length=4), nullable=True),
        sa.Column("piano_4", sa.String(length=4), nullable=True),
        sa.Column("gen_eff", sa.String(length=10), nullable=True),
        sa.Column("gen_regist", sa.String(length=10), nullable=True),
        sa.Column("gen_tipo", sa.String(length=1), nullable=True),
        sa.Column("gen_numero", sa.String(length=6), nullable=True),
        sa.Column("gen_progre", sa.String(length=3), nullable=True),
        sa.Column("gen_anno", sa.String(length=4), nullable=True),
        sa.Column("con_eff", sa.String(length=10), nullable=True),
        sa.Column("con_regist", sa.String(length=10), nullable=True),
        sa.Column("con_tipo", sa.String(length=1), nullable=True),
        sa.Column("con_numero", sa.String(length=6), nullable=True),
        sa.Column("con_progre", sa.String(length=3), nullable=True),
        sa.Column("con_anno", sa.String(length=4), nullable=True),
        sa.Column("partita", sa.String(length=7), nullable=True),
        sa.Column("annotazion", sa.String(length=200), nullable=True),
        sa.Column("mutaz_iniz", sa.Integer(), nullable=True),
        sa.Column("mutaz_fine", sa.Integer(), nullable=True),
        sa.Column("prot_notif", sa.String(length=18), nullable=True),
        sa.Column("data_notif", sa.String(length=8), nullable=True),
        sa.Column("gen_causa", sa.String(length=3), nullable=True),
        sa.Column("gen_descr", sa.String(length=100), nullable=True),
        sa.Column("con_causa", sa.String(length=3), nullable=True),
        sa.Column("con_descr", sa.String(length=100), nullable=True),
        sa.Column("flag_class", sa.String(length=1), nullable=True),
        sa.PrimaryKeyConstraint(
            "codice",
            "sezione",
            "immobile",
            "tipo_imm",
            "progressiv",
            name="cuarcuiu_pkey",
        ),
        schema="ctcn",
        comment="caratteristiche dell'unita' immobiliare",
    )


def downgrade() -> None:
    op.drop_table("cuarcuiu", schema="ctcn")
