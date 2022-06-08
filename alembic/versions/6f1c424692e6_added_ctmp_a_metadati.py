"""Added ctmp_a.metadati

Revision ID: 6f1c424692e6
Revises: bbfee83aa727
Create Date: 2022-06-08 09:21:20.864181

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6f1c424692e6'
down_revision = 'bbfee83aa727'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('metadati',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=False,
                              comment='Identificativo univoco della tabella'),
                    sa.Column('tipo_mappa', sa.String(length=100), nullable=False,
                              comment='Tipo di mappa, valori: MAPPA, MAPPA FONDIARIO, QUADRO DUNIONE'),
                    sa.Column('nome_mappa', sa.String(length=11), nullable=False,
                              comment='Nome della mappa, coincide con il nome del file CXF'),
                    sa.Column('scala', sa.String(length=12), nullable=False,
                              comment='Fattore di scala della mappa cartacea originaria'),
                    sa.Column('data_gen', sa.String(length=10), nullable=False,
                              comment='Data di generazione del file SUP'),
                    sa.Column('n_fabbric', sa.String(length=10), nullable=True,
                              comment='Numero totale di fabbricati'),
                    sa.Column('n_partic', sa.String(length=10), nullable=True,
                              comment='Numero totale di particelle'),
                    sa.Column('n_strade', sa.String(length=10), nullable=True,
                              comment='Numero totale di strade'),
                    sa.Column('n_acque', sa.String(length=10), nullable=True,
                              comment='Numero totale di acque'),
                    sa.Column('n_svil_all', sa.String(length=10), nullable=True,
                              comment='Numero totale di buchi relativi a sviluppi e allegati'),
                    sa.Column('fabbric', sa.String(length=10), nullable=True,
                              comment='Area totale di tutti i fabbricati'),
                    sa.Column('partic', sa.String(length=10), nullable=True,
                              comment='Area totale di tutte le particelle'),
                    sa.Column('strade', sa.String(length=10), nullable=True,
                              comment='Area totale di tutte le strade'),
                    sa.Column('acque', sa.String(length=10), nullable=True,
                              comment='Area totale di tutte le acque'),
                    sa.Column('svil_all', sa.String(length=10), nullable=True,
                              comment='Area totale di tutti i buchi relativi a sviluppi e allegati'),
                    sa.Column('totale', sa.String(length=10), nullable=True,
                              comment='Area somma delle aree di particelle, strade, acque, sviluppi e allegati'),
                    sa.Column('confine', sa.String(length=10), nullable=True,
                              comment='Area totale del confine della mappa'),
                    sa.Column('sbilancio', sa.String(length=10), nullable=True,
                              comment='Differenza tra totale e il confine'),
                    sa.Column('data_elab', sa.TIMESTAMP(), nullable=False,
                              comment='Data di generazione della mappa'),
                    sa.Column('stato', sa.Integer(), nullable=False,
                              comment='Stato del record, valori: 1, 2; 1 per record modificato in seguito'
                                      ' ad una trasformazione, 2 per record cancellato in seguito '
                                      'ad una nuova importazione'),
                    sa.Column('data_crea', sa.TIMESTAMP(), nullable=False,
                              comment='Data di creazione del record'),
                    sa.PrimaryKeyConstraint('id', 'stato', name='metadati_pkey'),
                    schema='ctmp_a',
                    comment='Dati riferiti alle importazioni dai file CXF e dai file SUP'
                    )
    op.create_index('metadati_i1', 'metadati', ["nome_mappa", "data_elab"],
                    schema='ctmp_a', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('metadati_i1', table_name='metadati', schema='ctmp_a', postgresql_using='btree')
    op.drop_table('metadati', schema='ctmp_a')
