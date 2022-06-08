"""Added ctmp_a.acque

Revision ID: c40bba6be47a
Revises: 713b8e1036cc
Create Date: 2022-06-08 08:36:37.207963

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga

# revision identifiers, used by Alembic.
revision = 'c40bba6be47a'
down_revision = '713b8e1036cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('acque',
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
                    sa.Column('numero', sa.String(length=9), nullable=True,
                              comment='Eventuale codice identificativo dell''acqua '
                                      'presente nelle mappe di tipo FONDIARIO'),
                    sa.Column('t_altezza', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Altezza in metri del testo associato'),
                    sa.Column('t_angolo', sa.Numeric(precision=12, scale=2), nullable=True,
                              comment='Angolo in gradi che il testo associato forma con l''asse orizzontale'),
                    sa.Column('t_pt_ins', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Punto di inserimento del testo associato'),
                    sa.Column('t_ln_anc', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Eventuale linea di ancoraggio tra il punto di inserimento'
                                      ' del testo ed un punto interno al contorno'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=False,
                              comment='Geometria del contorno dell''acqua'),
                    sa.Column('data_gen', sa.String(length=10), nullable=False,
                              comment='Data di generazione della mappa'),
                    sa.Column('stato', sa.Integer(), nullable=False,
                              comment='Stato del record, valori: 1, 2; 1 per record modificato in seguito'
                                      ' ad una trasformazione, 2 per record cancellato in seguito '
                                      'ad una nuova importazione'),
                    sa.Column('data_crea', sa.TIMESTAMP(), nullable=False,
                              comment='Data di creazione del record'),
                    sa.PrimaryKeyConstraint('id', name='acque_pkey'),
                    schema='ctmp_a',
                    comment='Contorni delle acque'
                    )
    op.drop_index('idx_acque_t_pt_ins', table_name='acque', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('idx_acque_t_ln_anc', table_name='acque', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('idx_acque_geom', table_name='acque', schema='ctmp_a', postgresql_using='gist')
    op.create_index('acque_i1', 'acque', ["comune", "sezione", "foglio", "allegato", "sviluppo", "numero"],
                    schema='ctmp_a', postgresql_using='btree')
    op.create_index('acque_si1', 'acque', ['geom'], schema='ctmp_a', postgresql_using='gist')
    op.create_index('acque_si2', 'acque', ['t_pt_ins'], schema='ctmp_a', postgresql_using='gist')
    op.create_index('acque_si3', 'acque', ['t_ln_anc'], schema='ctmp_a', postgresql_using='gist')


def downgrade() -> None:
    op.drop_index('acque_i1', table_name='acque', schema='ctmp_a', postgresql_using='btree')
    op.drop_index('acque_si1', table_name='acque', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('acque_si2', table_name='acque', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('acque_si3', table_name='acque', schema='ctmp_a', postgresql_using='gist')
    op.drop_table('acque', schema='ctmp_a')
