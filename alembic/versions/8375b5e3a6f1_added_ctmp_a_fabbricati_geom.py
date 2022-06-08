"""Added ctmp_a.fabbricati.geom

Revision ID: 8375b5e3a6f1
Revises: 6f1c424692e6
Create Date: 2022-06-08 09:43:48.246678

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga


# revision identifiers, used by Alembic.
revision = '8375b5e3a6f1'
down_revision = '6f1c424692e6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('fabbricati.geom',
                    sa.Column('id_0', sa.BigInteger(), nullable=False),
                    sa.Column('geom', ga.types.Geometry(
                        from_text='ST_GeomFromEWKT', name='geometry',
                        geometry_type='POLYGON', srid=25833
                    ),
                              nullable=True,
                              comment=''),
                    sa.Column('id', sa.Integer(), nullable=True,
                              comment='Identificativo univoco della tabella'),
                    sa.Column('comune', sa.String(length=4), nullable=True,
                              comment='Codice catastale del Comune'),
                    sa.Column('sezione', sa.String(length=1), nullable=True,
                              comment='Codice sezione censuaria'),
                    sa.Column('foglio', sa.String(length=4), nullable=True,
                              comment='Codice identificativo del foglio'),
                    sa.Column('allegato', sa.String(length=1), nullable=True,
                              comment='Eventuale codice allegato'),
                    sa.Column('sviluppo', sa.String(length=1), nullable=True,
                              comment='Eventuale codice sviluppo'),
                    sa.Column('numero', sa.String(length=9), nullable=True,
                              comment='Codice identificativo della particella contenente il fabbricato'),
                    sa.Column('t_altezza', sa.Float(), nullable=True,
                              comment='Altezza in metri del testo associato'),
                    sa.Column('t_angolo', sa.Float(), nullable=True,
                              comment='Angolo in gradi che il testo associato forma con lasse orizzontale'),
                    sa.Column('t_pt_ins', sa.String(), nullable=True,
                              comment='Punto di inserimento del testo associato'),
                    sa.Column('t_ln_anc', sa.String(), nullable=True,
                              comment='Eventuale linea di ancoraggio tra il punto di inserimento '
                                      'del testo ed un punto interno al fabbricato'),
                    sa.Column('data_gen', sa.String(length=10), nullable=False,
                              comment='Data di generazione della mappa'),
                    sa.Column('stato', sa.Integer(), nullable=False,
                              comment='Stato del record, valori: 1, 2; 1 per record modificato in seguito'
                                      ' ad una trasformazione, 2 per record cancellato in seguito '
                                      'ad una nuova importazione'),
                    sa.Column('data_crea', sa.TIMESTAMP(), nullable=False,
                              comment='Data di creazione del record'),
                    sa.PrimaryKeyConstraint('id_0', name='fabbricati.geom_pkey'),
                    schema='ctmp_a'
                    )
    op.drop_index('idx_fabbricati.geom_geom', table_name='fabbricati.geom', schema='ctmp_a', postgresql_using='gist')


def downgrade() -> None:
    op.drop_table('fabbricati.geom', schema='ctmp_a')
