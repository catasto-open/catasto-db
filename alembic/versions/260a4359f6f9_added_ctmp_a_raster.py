"""Added ctmp_a.raster

Revision ID: 260a4359f6f9
Revises: 00641d8d18f3
Create Date: 2022-06-08 09:11:17.804967

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga


# revision identifiers, used by Alembic.
revision = "260a4359f6f9"
down_revision = "00641d8d18f3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raster",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
            autoincrement=False,
            comment="Identificativo univoco della tabella",
        ),
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
            nullable=True,
            comment="Eventuale codice allegato",
        ),
        sa.Column(
            "sviluppo",
            sa.String(length=1),
            nullable=True,
            comment="Eventuale codice sviluppo",
        ),
        sa.Column(
            "nome_file",
            sa.String(length=80),
            nullable=True,
            comment="Nome del file raster",
        ),
        sa.Column(
            "geom",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=False,
            comment="Geometria del riquadro rappresentante il posizionamento georiferito del raster",
        ),
        sa.Column(
            "data_gen",
            sa.String(length=10),
            nullable=False,
            comment="Data di generazione della mappa",
        ),
        sa.Column(
            "stato",
            sa.Integer(),
            nullable=False,
            comment="Stato del record, valori: 1, 2; 1 per record modificato in seguito"
            " ad una trasformazione, 2 per record cancellato in seguito "
            "ad una nuova importazione",
        ),
        sa.Column(
            "data_crea",
            sa.TIMESTAMP(),
            nullable=False,
            comment="Data di creazione del record",
        ),
        sa.PrimaryKeyConstraint("id", name="raster_pkey"),
        schema="ctmp_a",
        comment="File raster",
    )
    op.drop_index(
        "idx_raster_geom",
        table_name="raster",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.create_index(
        "raster_si1",
        "raster",
        ["geom"],
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.create_index(
        "raster_i1",
        "raster",
        ["comune", "sezione", "foglio", "allegato", "sviluppo"],
        schema="ctmp_a",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "raster_i1",
        table_name="raster",
        schema="ctmp_a",
        postgresql_using="btree",
    )
    op.drop_index(
        "raster_si1",
        table_name="raster",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.drop_table("raster", schema="ctmp_a")
