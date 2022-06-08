"""Added ctmp_a.simboli

Revision ID: b6e46485b370
Revises: 260a4359f6f9
Create Date: 2022-06-08 09:11:22.370245

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = 'b6e46485b370'
down_revision = '260a4359f6f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('simboli',
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
                              comment='Codice del tipo di simbolo'),
                    sa.Column('angolo', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Angolo in gradi che il simbolo forma con lasse orizzontale'),
                    sa.Column('esterno', sa.Integer(), nullable=False,
                              comment='Indica se lelemento si trova allesterno del confine della mappa'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'), nullable=False,
                              comment='Punto di inserimento del simbolo'),
                    sa.Column('data_gen', sa.String(length=10), nullable=False,
                              comment='Data di generazione della mappa'),
                    sa.Column('stato', sa.Integer(), nullable=False,
                              comment='Stato del record, valori: 1, 2; 1 per record modificato in seguito'
                                      ' ad una trasformazione, 2 per record cancellato in seguito '
                                      'ad una nuova importazione'),
                    sa.Column('data_crea', sa.TIMESTAMP(), nullable=False,
                              comment='Data di creazione del record'),
                    sa.PrimaryKeyConstraint('id', name='simboli_pkey'),
                    schema='ctmp_a',
                    comment='Simboli'
                    )
    op.drop_index('idx_simboli_geom', table_name='simboli', schema='ctmp_a', postgresql_using='gist')
    op.create_index('simboli_si1', 'simboli', ['geom'], unique=False, schema='ctmp_a', postgresql_using='gist')
    op.create_index('simboli_i1', 'simboli', ["comune", "sezione", "foglio", "allegato", "sviluppo"],
                    schema='ctmp_a', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('simboli_si1', table_name='simboli', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('simboli_i1', table_name='simboli', schema='ctmp_a', postgresql_using='btree')
    op.drop_table('simboli', schema='ctmp_a')
