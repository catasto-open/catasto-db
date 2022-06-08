"""Added ctmp_a.fiduciali

Revision ID: cd6344be316d
Revises: 9dfe60810b53
Create Date: 2022-06-08 08:42:50.554048

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga


# revision identifiers, used by Alembic.
revision = 'cd6344be316d'
down_revision = '9dfe60810b53'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('fiduciali',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False,
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
                    sa.Column('prog', sa.Integer(), nullable=False,
                              comment='Numero identificativo del fiduciale'),
                    sa.Column('codice', sa.Integer(), nullable=False,
                              comment='Codice del tipo di fiduciale'),
                    sa.Column('esterno', sa.Integer(), nullable=False,
                              comment='Indica se l''elemento si trova all''esterno del confine della mappa'),
                    sa.Column('t_pt_ins', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True,
                              comment='Punto di inserimento del numero identificativo associato al fiduciale'),
                    sa.Column('geom', ga.types.Geometry(from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=False,
                              comment='Punto di inserimento del fiduciale'),
                    sa.Column('data_gen', sa.String(length=10), nullable=False,
                              comment='Data di generazione della mappa'),
                    sa.Column('stato', sa.Integer(), nullable=False,
                              comment='Stato del record, valori: 1, 2; 1 per record modificato in seguito'
                                      ' ad una trasformazione, 2 per record cancellato in seguito '
                                      'ad una nuova importazione'),
                    sa.Column('data_crea', sa.TIMESTAMP(), nullable=False,
                              comment='Data di creazione del record'),
                    sa.PrimaryKeyConstraint('id', name='fiduciali_pkey'),
                    schema='ctmp_a',
                    comment='Punti fiduciali'
                    )
    op.drop_index('idx_fiduciali_geom', table_name='fiduciali', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('idx_fiduciali_t_pt_ins', table_name='fiduciali', schema='ctmp_a', postgresql_using='gist')

    op.create_index('fiduciali_si1', 'fiduciali', ['geom'], unique=False, schema='ctmp_a', postgresql_using='gist')
    op.create_index('fiduciali_si2', 'fiduciali', ['t_pt_ins'], unique=False, schema='ctmp_a', postgresql_using='gist')
    op.create_index('fiduciali_i1', 'fiduciali', ["comune", "sezione", "foglio", "allegato", "sviluppo"],
                    schema='ctmp_a', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('fiduciali_i1', table_name='fiduciali', schema='ctmp_a', postgresql_using='btree')
    op.drop_index('fiduciali_si1', table_name='fiduciali', schema='ctmp_a', postgresql_using='gist')
    op.drop_index('fiduciali_si2', table_name='fiduciali', schema='ctmp_a', postgresql_using='gist')
    op.drop_table('fiduciali', schema='ctmp_a')
