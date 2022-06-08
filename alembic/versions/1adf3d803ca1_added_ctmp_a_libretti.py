"""Added ctmp_a.libretti

Revision ID: 1adf3d803ca1
Revises: 190ca23c6a14
Create Date: 2022-06-08 08:58:39.679459

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga


# revision identifiers, used by Alembic.
revision = '1adf3d803ca1'
down_revision = '190ca23c6a14'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('libretti',
                    sa.Column('id',  sa.Integer(), nullable=False, autoincrement=False,
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
                    sa.Column('protocollo', sa.String(length=80), nullable=True,
                              comment='Numero di protocollo del libretto'),
                    sa.Column('codice', sa.Integer(), nullable=False,
                              comment='Codice del tipo di tratto della linea'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=False,
                              comment='Geometria del libretto'),
                    sa.Column('data_gen', sa.String(length=10), nullable=False,
                              comment='Data di generazione della mappa'),
                    sa.Column('stato', sa.Integer(), nullable=False,
                              comment='Stato del record, valori: 1, 2; 1 per record modificato in seguito'
                                      ' ad una trasformazione, 2 per record cancellato in seguito '
                                      'ad una nuova importazione'),
                    sa.Column('data_crea', sa.TIMESTAMP(), nullable=False,
                              comment='Data di creazione del record'),
                    sa.PrimaryKeyConstraint('id', name='libretti_pkey'),
                    schema='ctmp_a',
                    comment='Libretti'
                    )
    op.drop_index('idx_libretti_geom', table_name='libretti', schema='ctmp_a', postgresql_using='gist')
    op.create_index('libretti_si1', 'libretti', ['geom'], schema='ctmp_a', postgresql_using='gist')
    op.create_index('libretti_i1', 'libretti', ["comune", "sezione", "foglio", "allegato", "sviluppo"],
                    schema='ctmp_a', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('libretti_si1', table_name='libretti', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('libretti_i1', table_name='libretti', schema='ctmp_a', postgresql_using='btree')
    op.drop_table('libretti', schema='ctmp_a')
