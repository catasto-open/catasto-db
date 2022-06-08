"""Added ctmp.strade

Revision ID: dc7ebc9801d4
Revises: abb09b71e194
Create Date: 2022-06-08 00:02:51.318624

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = 'dc7ebc9801d4'
down_revision = 'abb09b71e194'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('strade',
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
                    sa.Column('numero', sa.String(length=9), nullable=True,
                              comment='Eventuale codice identificativo della strada '
                                      'presente nelle mappe di tipo FONDIARIO'),
                    sa.Column('t_altezza', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Altezza in metri del testo associato'),
                    sa.Column('t_angolo', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Angolo in gradi che il testo associato forma con lasse orizzontale'),
                    sa.Column('t_pt_ins', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Punto di inserimento del testo associato'),
                    sa.Column('t_ln_anc', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Eventuale linea di ancoraggio tra il punto di inserimento del '
                                      'testo ed un punto interno al contorno'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=False,
                              comment='Geometria del contorno della strada'),
                    sa.PrimaryKeyConstraint('id', name='strade_pkey'),
                    schema='ctmp',
                    comment='Contorni delle strade'
                    )
    op.drop_index('idx_strade_t_pt_ins', table_name='strade', schema='ctmp', postgresql_using='gist')
    op.drop_index('idx_strade_t_ln_anc', table_name='strade', schema='ctmp', postgresql_using='gist')
    op.drop_index('idx_strade_geom', table_name='strade', schema='ctmp', postgresql_using='gist')
    
    op.create_index('strade_si1', 'strade', ['geom'], schema='ctmp', postgresql_using='gist')
    op.create_index('strade_si2', 'strade', ['t_pt_ins'], schema='ctmp', postgresql_using='gist')
    op.create_index('strade_si3', 'strade', ['t_ln_anc'], schema='ctmp', postgresql_using='gist')
    op.create_index('strade_i1', 'strade', ["comune", "sezione", "foglio", "allegato", "sviluppo", "numero"],
                    schema='ctmp', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('strade_si1', table_name='strade', schema='ctmp', postgresql_using='gist')
    op.drop_index('strade_si2', table_name='strade', schema='ctmp', postgresql_using='gist')
    op.drop_index('strade_si3', table_name='strade', schema='ctmp', postgresql_using='gist')
    op.drop_index('strade_i1', table_name='strade', schema='ctmp', postgresql_using='btree')
    op.drop_table('strade', schema='ctmp')
