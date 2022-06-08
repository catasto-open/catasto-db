"""Added ctmp.libretti

Revision ID: 3962da0abb5a
Revises: da2495bff3f7
Create Date: 2022-06-07 21:56:35.201612

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = '3962da0abb5a'
down_revision = 'da2495bff3f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('libretti',
                    sa.Column('id', sa.BigInteger(), nullable=False,
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
                    sa.PrimaryKeyConstraint('id', name='libretti_pkey'),
                    schema='ctmp',
                    comment='Libretti'
                    )
    op.drop_index('idx_libretti_geom', table_name='libretti', schema='ctmp', postgresql_using='gist')
    op.create_index('libretti_si1', 'libretti', ['geom'], schema='ctmp', postgresql_using='gist')
    op.create_index('libretti_i1', 'libretti', ["comune", "sezione", "foglio", "allegato", "sviluppo"],
                    schema='ctmp', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('libretti_si1', table_name='libretti', schema='ctmp', postgresql_using='gist')
    op.drop_index('libretti_i1', table_name='libretti', schema='ctmp', postgresql_using='btree')
    op.drop_table('libretti', schema='ctmp')
