"""Added ctmp.fogli

Revision ID: da2495bff3f7
Revises: 9414dbb7aaae
Create Date: 2022-06-07 21:34:03.112632

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = 'da2495bff3f7'
down_revision = '9414dbb7aaae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('fogli',
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
                    sa.Column('t_altezza', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Altezza in metri del testo associato'),
                    sa.Column('t_angolo', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Angolo in gradi che il testo associato forma con l''asse orizzontale'),
                    sa.Column('t_pt_ins', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Punto di inserimento del testo associato'),
                    sa.Column('t_ln_anc', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Eventuale linea di ancoraggio tra il punto di'
                                      ' inserimento del testo ed un punto interno al foglio'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'), nullable=False,
                              comment='Geometria del foglio'),
                    sa.PrimaryKeyConstraint('id', name='fogli_pkey'),
                    schema='ctmp'
                    )
    op.drop_index('idx_fogli_t_pt_ins', table_name='fogli', schema='ctmp', postgresql_using='gist')
    op.drop_index('idx_fogli_t_ln_anc', table_name='fogli', schema='ctmp', postgresql_using='gist')
    op.drop_index('idx_fogli_geom', table_name='fogli', schema='ctmp', postgresql_using='gist')
    op.create_index('fogli_i1', 'fogli', ["comune", "sezione", "foglio", "allegato", "sviluppo"],
                    schema='ctmp', postgresql_using='btree')
    op.create_index('fogli_si1', 'fogli', ['geom'], schema='ctmp', postgresql_using='gist')
    op.create_index('fogli_si2', 'fogli', ['t_pt_ins'], schema='ctmp', postgresql_using='gist')
    op.create_index('fogli_si3', 'fogli', ['t_ln_anc'], schema='ctmp', postgresql_using='gist')


def downgrade() -> None:
    op.drop_index('fogli_i1', table_name='fogli', schema='ctmp', postgresql_using='btree')
    op.drop_index('fogli_si1', table_name='fogli', schema='ctmp', postgresql_using='gist')
    op.drop_index('fogli_si2', table_name='fogli', schema='ctmp', postgresql_using='gist')
    op.drop_index('fogli_si3', table_name='fogli', schema='ctmp', postgresql_using='gist')
    op.drop_table('fogli', schema='ctmp')
