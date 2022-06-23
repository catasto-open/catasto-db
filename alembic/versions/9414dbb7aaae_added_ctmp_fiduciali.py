"""Added ctmp.fiduciali

Revision ID: 9414dbb7aaae
Revises: ab1c5d2cc591
Create Date: 2022-06-07 21:09:45.286859

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = "9414dbb7aaae"
down_revision = "ab1c5d2cc591"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "fiduciali",
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
            "prog",
            sa.Integer(),
            nullable=False,
            comment="Numero identificativo del fiduciale",
        ),
        sa.Column(
            "codice",
            sa.Integer(),
            nullable=False,
            comment="Codice del tipo di fiduciale",
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
            "t_pt_ins",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=True,
            comment="Punto di inserimento del numero identificativo associato al fiduciale",
        ),
        sa.Column(
            "geom",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=False,
            comment="Punto di inserimento del fiduciale",
        ),
        sa.PrimaryKeyConstraint("id", name="fiduciali_pkey"),
        schema="ctmp",
        comment="Punti fiduciali",
    )
    op.drop_index(
        "idx_fiduciali_geom",
        table_name="fiduciali",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_index(
        "idx_fiduciali_t_pt_ins",
        table_name="fiduciali",
        schema="ctmp",
        postgresql_using="gist",
    )

    op.create_index(
        "fiduciali_si1",
        "fiduciali",
        ["geom"],
        unique=False,
        schema="ctmp",
        postgresql_using="gist",
    )
    op.create_index(
        "fiduciali_si2",
        "fiduciali",
        ["t_pt_ins"],
        unique=False,
        schema="ctmp",
        postgresql_using="gist",
    )
    op.create_index(
        "fiduciali_i1",
        "fiduciali",
        ["comune", "sezione", "foglio", "allegato", "sviluppo"],
        schema="ctmp",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "fiduciali_i1",
        table_name="fiduciali",
        schema="ctmp",
        postgresql_using="btree",
    )
    op.drop_index(
        "fiduciali_si1",
        table_name="fiduciali",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_index(
        "fiduciali_si2",
        table_name="fiduciali",
        schema="ctmp",
        postgresql_using="gist",
    )
    op.drop_table("fiduciali", schema="ctmp")
