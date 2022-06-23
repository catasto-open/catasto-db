"""Added ctmp.raster

Revision ID: e983d2bd40eb
Revises: 7ea7f10fddd4
Create Date: 2022-06-07 23:36:37.908768

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = "e983d2bd40eb"
down_revision = "7ea7f10fddd4"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raster",
        sa.Column(
            "id",
            sa.BigInteger(),
            nullable=False,
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
        sa.PrimaryKeyConstraint("id", name="raster_pkey"),
        schema="ctmp",
        comment="File raster",
    )
    op.drop_index(
        "idx_raster_geom",
        table_name="raster",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.create_index(
        "raster_si1",
        "raster",
        ["geom"],
        schema="ctmp",
        postgresql_using="gist",
    )
    op.create_index(
        "raster_i1",
        "raster",
        ["comune", "sezione", "foglio", "allegato", "sviluppo"],
        schema="ctmp",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "raster_i1",
        table_name="raster",
        schema="ctmp",
        postgresql_using="btree",
    )
    op.drop_index(
        "raster_si1",
        table_name="raster",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_table("raster", schema="ctmp")
