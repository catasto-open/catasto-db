"""Added ctmp.particelle

Revision ID: b233443808c5
Revises: 9152e3914ca5
Create Date: 2022-06-07 22:44:37.210406

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = 'b233443808c5'
down_revision = '9152e3914ca5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('particelle',
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
                              comment='Codice identificativo della particella'),
                    sa.Column('t_altezza', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Altezza in metri del testo associato'),
                    sa.Column('t_angolo', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Angolo in gradi che il testo associato forma con l''asse orizzontale'),
                    sa.Column('t_pt_ins', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Punto di inserimento del testo associato'),
                    sa.Column('t_ln_anc', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Eventuale linea di ancoraggio tra il punto di '
                                      'inserimento del testo ed un punto interno alla particella'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=False,
                              comment='Geometria della particella'),
                    sa.PrimaryKeyConstraint('id', name='particelle_pkey'),
                    schema='ctmp',
                    comment='Particelle'
                    )
    op.drop_index('idx_particelle_t_pt_ins', table_name='particelle', schema='ctmp', postgresql_using='gist')
    op.drop_index('idx_particelle_t_ln_anc', table_name='particelle', schema='ctmp', postgresql_using='gist')
    op.drop_index('idx_particelle_geom', table_name='particelle', schema='ctmp', postgresql_using='gist')
    op.create_index('particelle_i1', 'particelle', ["comune", "sezione", "foglio", "allegato", "sviluppo", "numero"],
                    schema='ctmp', postgresql_using='btree')
    op.create_index('particelle_si1', 'particelle', ['geom'], schema='ctmp', postgresql_using='gist')
    op.create_index('particelle_si2', 'particelle', ['t_pt_ins'], schema='ctmp',
                    postgresql_using='gist')
    op.create_index('particelle_si3', 'particelle', ['t_ln_anc'], schema='ctmp',
                    postgresql_using='gist')


def downgrade() -> None:
    op.drop_index('particelle_i1', table_name='particelle', schema='ctmp', postgresql_using='btree')
    op.drop_index('particelle_si1', table_name='particelle', schema='ctmp', postgresql_using='gist')
    op.drop_index('particelle_si2', table_name='particelle', schema='ctmp', postgresql_using='gist')
    op.drop_index('particelle_si3', table_name='particelle', schema='ctmp', postgresql_using='gist')
    op.drop_table('particelle', schema='ctmp')
