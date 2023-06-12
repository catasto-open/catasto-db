"""Added ctmp.punti_controllo

Revision ID: 98f0763b30b0
Revises: b233443808c5
Create Date: 2022-06-07 23:05:25.265409

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = "98f0763b30b0"
down_revision = "b233443808c5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "punti_controllo",
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
            "numero",
            sa.String(length=9),
            nullable=True,
            comment="Codice identificativo della particella",
        ),
        sa.Column(
            "n_gruppo",
            sa.Integer(),
            nullable=False,
            comment="Numero ordinale del gruppo di punti",
        ),
        sa.Column(
            "n_punto",
            sa.Integer(),
            nullable=False,
            comment="Numero ordinale del punto di controllo",
        ),
        sa.Column(
            "pt_orig",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=False,
            comment="Geometria del punto di origine",
        ),
        sa.Column(
            "pt_dest",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=False,
            comment="Geometria del punto di destinazione",
        ),
        sa.PrimaryKeyConstraint(
            "comune",
            "sezione",
            "foglio",
            "n_gruppo",
            "n_punto",
            name="punti_controllo_pkey",
        ),
        schema="ctmp",
        comment="Punti di controllo per la trasformazione geometrica delle mappe",
    )
    op.drop_index(
        "idx_punti_controllo_pt_orig",
        table_name="punti_controllo",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_index(
        "idx_punti_controllo_pt_dest",
        table_name="punti_controllo",
        schema="ctmp",
        postgresql_using="gist",
    )

    op.create_index(
        "punti_controllo_si1",
        "punti_controllo",
        ["pt_orig"],
        unique=False,
        schema="ctmp",
        postgresql_using="gist",
    )
    op.create_index(
        "punti_controllo_si2",
        "punti_controllo",
        ["pt_dest"],
        unique=False,
        schema="ctmp",
        postgresql_using="gist",
    )


def downgrade() -> None:
    op.drop_index(
        "punti_controllo_si1",
        table_name="punti_controllo",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_index(
        "punti_controllo_si2",
        table_name="punti_controllo",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_table("punti_controllo", schema="ctmp")
