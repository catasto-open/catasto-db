"""Added ctmp_a.quadri_unione

Revision ID: 00641d8d18f3
Revises: 4ad75aaea060
Create Date: 2022-06-08 09:06:44.980864

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga


# revision identifiers, used by Alembic.
revision = "00641d8d18f3"
down_revision = "4ad75aaea060"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "quadri_unione",
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
            "t_altezza",
            sa.Numeric(precision=12, scale=2),
            nullable=True,
            comment="Altezza in metri del testo associato",
        ),
        sa.Column(
            "t_angolo",
            sa.Numeric(precision=12, scale=2),
            nullable=True,
            comment="Angolo in gradi che il testo associato forma con l"
            "asse orizzontale",
        ),
        sa.Column(
            "t_pt_ins",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=True,
            comment="Punto di inserimento del testo associato",
        ),
        sa.Column(
            "t_ln_anc",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=True,
            comment="Eventuale linea di ancoraggio tra il punto di inserimento "
            "del testo ed un punto interno al foglio",
        ),
        sa.Column(
            "geom",
            ga.types.Geometry(from_text="ST_GeomFromEWKT", name="geometry"),
            nullable=False,
            comment="Geometria del foglio",
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
        sa.PrimaryKeyConstraint("id", name="quadri_unione_pkey"),
        schema="ctmp_a",
        comment="Fogli",
    )
    op.drop_index(
        "idx_quadri_unione_t_pt_ins",
        table_name="quadri_unione",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.drop_index(
        "idx_quadri_unione_t_ln_anc",
        table_name="quadri_unione",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.drop_index(
        "idx_quadri_unione_geom",
        table_name="quadri_unione",
        schema="ctmp_a",
        postgresql_using="gist",
    )

    op.create_index(
        "quadri_unione_si1",
        "quadri_unione",
        ["geom"],
        unique=False,
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.create_index(
        "quadri_unione_si2",
        "quadri_unione",
        ["t_pt_ins"],
        unique=False,
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.create_index(
        "quadri_unione_si3",
        "quadri_unione",
        ["t_ln_anc"],
        unique=False,
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.create_index(
        "quadri_unione_i1",
        "quadri_unione",
        ["comune", "sezione", "foglio", "allegato", "sviluppo"],
        schema="ctmp_a",
        postgresql_using="btree",
    )


def downgrade() -> None:
    op.drop_index(
        "quadri_unione_si1",
        table_name="quadri_unione",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.drop_index(
        "quadri_unione_si2",
        table_name="quadri_unione",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.drop_index(
        "quadri_unione_si3",
        table_name="quadri_unione",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.drop_index(
        "quadri_unione_i1",
        table_name="quadri_unione",
        schema="ctmp_a",
        postgresql_using="gist",
    )
    op.drop_table("quadri_unione", schema="ctmp_a")
