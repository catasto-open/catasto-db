"""Added ctcn.metadati

Revision ID: 1f81a8a100e8
Revises: 05cf7b1812ee
Create Date: 2022-06-07 17:38:21.176047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f81a8a100e8'
down_revision = '05cf7b1812ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('metadati',
                    sa.Column('estrazione', sa.String(length=20), nullable=False,
                              comment='Nome del file della fornitura'),
                    sa.Column('comune', sa.String(length=4), nullable=True,
                              comment='Comune richiesto'),
                    sa.Column('sezione', sa.String(length=4), nullable=True,
                              comment='Sezione del comune richiesto'),
                    sa.Column('data_rich', sa.String(length=10), nullable=True,
                              comment='Data della richiesta'),
                    sa.Column('data_elab', sa.String(length=10), nullable=True,
                              comment='Data di elaborazione della fornitura'),
                    sa.Column('tipo_estr', sa.String(length=100), nullable=True,
                              comment='Tipologia di estrazione della richiesta'),
                    sa.Column('data_selez', sa.String(length=10), nullable=True,
                              comment='Data di riferimento per la selezione (solo per attualita)'),
                    sa.Column('date_reg', sa.String(length=50), nullable=True,
                              comment='Data iniziale e finale intervallo '
                                      '(solo se aggiornamenti per data di registrazione)'),
                    sa.Column('numero_rec', sa.String(length=20), nullable=True,
                              comment='Numero di record estratti'),
                    schema='ctcn',
                    comment='Dati riferiti alle importazioni eseguite'
                    )
    op.create_index('metadati_idx1', 'metadati', ['comune', 'sezione'],
                    schema='ctcn', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('metadati_idx1', table_name='metadati', schema='ctcn', postgresql_using='btree')
    op.drop_table('metadati', schema='ctcn')
