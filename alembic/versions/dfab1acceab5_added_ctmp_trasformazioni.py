"""Added ctmp.trasformazioni

Revision ID: dfab1acceab5
Revises: 5c8b78c99c64
Create Date: 2022-06-08 08:29:57.163312

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "dfab1acceab5"
down_revision = "5c8b78c99c64"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "trasformazioni",
        sa.Column(
            "comune",
            sa.String(length=4),
            nullable=False,
            comment="Codice catastale del Comune",
        ),
        sa.Column(
            "sezione",
            sa.String(length=1),
            nullable=False,
            comment="Codice sezione censuaria",
        ),
        sa.Column(
            "foglio",
            sa.String(length=4),
            nullable=False,
            comment="Codice identificativo del foglio",
        ),
        sa.Column(
            "allegato",
            sa.String(length=1),
            nullable=False,
            comment="Eventuale codice allegato",
        ),
        sa.Column(
            "sviluppo",
            sa.String(length=1),
            nullable=False,
            comment="Eventuale codice sviluppo",
        ),
        sa.Column(
            "n_trasf",
            sa.Integer(),
            nullable=False,
            comment="Numero ordinale della trasformazione",
        ),
        sa.Column(
            "tipo_trasf",
            sa.String(length=20),
            nullable=False,
            comment="Codice del tipo di trasformazione",
        ),
        sa.Column(
            "punti_contr",
            sa.Float(),
            nullable=False,
            comment="Punti di controllo usati per creare la matrice di trasformazione",
        ),
        sa.Column(
            "matrice_trasf",
            sa.Float(),
            nullable=False,
            comment="Matrice di trasformazione",
        ),
        sa.PrimaryKeyConstraint(
            "comune",
            "sezione",
            "foglio",
            "allegato",
            "sviluppo",
            "n_trasf",
            name="trasformazioni_pkey",
        ),
        schema="ctmp",
        comment="Trasformazioni eseguite sui fogli",
    )


def downgrade() -> None:
    op.drop_table("trasformazioni", schema="ctmp")
