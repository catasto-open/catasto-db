"""Added ctmp.linee_vest

Revision ID: 2507f2e1e507
Revises: 3962da0abb5a
Create Date: 2022-06-07 22:11:07.011215

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = "2507f2e1e507"
down_revision = "3962da0abb5a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "linee_vest",
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
            "codice",
            sa.Integer(),
            nullable=False,
            comment="Codice del tipo di tratto",
        ),
        sa.Column(
            "esterno",
            sa.Integer(),
            nullable=False,
            comment="Indica se l"
            "elemento si trova all"
            "esterno del confine della mappa",
        ),
        sa.Column(
            "geom",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=False,
            comment="Geometria della linea",
        ),
        sa.PrimaryKeyConstraint("id", name="linee_vest_pkey"),
        schema="ctmp",
        comment="Linee di vestizione",
    )
    op.drop_index(
        "idx_linee_vest_geom",
        table_name="linee_vest",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.create_index(
        "linee_vest_si1",
        "linee_vest",
        ["geom"],
        schema="ctmp",
        postgresql_using="gist",
    )
    op.create_index(
        "linee_vest_i1",
        "linee_vest",
        ["comune", "sezione", "foglio", "allegato", "sviluppo"],
        schema="ctmp",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "linee_vest_si1",
        table_name="linee_vest",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_index(
        "linee_vest_i1",
        table_name="linee_vest",
        schema="ctmp",
        postgresql_using="btree",
    )
    op.drop_table("linee_vest", schema="ctmp")
