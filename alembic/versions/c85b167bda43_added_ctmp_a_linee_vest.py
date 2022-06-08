"""Added ctmp_a.linee_vest

Revision ID: c85b167bda43
Revises: 1adf3d803ca1
Create Date: 2022-06-08 08:58:51.477735

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga


# revision identifiers, used by Alembic.
revision = 'c85b167bda43'
down_revision = '1adf3d803ca1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('linee_vest',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=False,
                              comment='Identificativo univoco della tabella'),
                    sa.Column('comune', sa.String(length=4), nullable=False,
                              comment='Codice catastale del Comune'),
                    sa.Column('sezione', sa.String(length=1), nullable=False,
                              comment='Codice sezione censuaria'),
                    sa.Column('foglio', sa.String(length=4), nullable=False,
                              comment='Codice identificativo del foglio'),
                    sa.Column('allegato', sa.String(length=1), nullable=True,
                              comment='Eventuale codice allegato'),
                    sa.Column('sviluppo', sa.String(length=1), nullable=True,
                              comment='Eventuale codice sviluppo'),
                    sa.Column('codice', sa.Integer(), nullable=False,
                              comment='Codice del tipo di tratto'),
                    sa.Column('esterno', sa.Integer(), nullable=False,
                              comment='Indica se l''elemento si trova all''esterno del confine della mappa'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'), nullable=False,
                              comment='Geometria della linea'),
                    sa.Column('data_gen', sa.String(length=10), nullable=False,
                              comment='Data di generazione della mappa'),
                    sa.Column('stato', sa.Integer(), nullable=False,
                              comment='Stato del record, valori: 1, 2; 1 per record modificato in seguito'
                                      ' ad una trasformazione, 2 per record cancellato in seguito '
                                      'ad una nuova importazione'),
                    sa.Column('data_crea', sa.TIMESTAMP(), nullable=False,
                              comment='Data di creazione del record'),
                    sa.PrimaryKeyConstraint('id', name='linee_vest_pkey'),
                    schema='ctmp_a',
                    comment='Linee di vestizione',
                    )
    op.drop_index('idx_linee_vest_geom', table_name='linee_vest', schema='ctmp_a', postgresql_using='gist')
    op.create_index('linee_vest_si1', 'linee_vest', ['geom'], schema='ctmp_a', postgresql_using='gist')
    op.create_index('linee_vest_i1', 'linee_vest', ["comune", "sezione", "foglio", "allegato", "sviluppo"],
                    schema='ctmp_a', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('linee_vest_si1', table_name='linee_vest', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('linee_vest_i1', table_name='linee_vest', schema='ctmp_a', postgresql_using='btree')
    op.drop_table('linee_vest', schema='ctmp_a')
