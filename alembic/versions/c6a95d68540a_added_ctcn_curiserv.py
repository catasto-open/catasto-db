"""Added ctcn.curiserv

Revision ID: c6a95d68540a
Revises: e3f49243636f
Create Date: 2022-06-07 16:50:15.282735

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c6a95d68540a'
down_revision = 'e3f49243636f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('curiserv',
                    sa.Column('codice', sa.String(length=4), nullable=False),
                    sa.Column('sezione', sa.String(length=1), nullable=False),
                    sa.Column('immobile', sa.BigInteger(), nullable=False),
                    sa.Column('tipo_imm', sa.String(length=1), nullable=False),
                    sa.Column('progressiv', sa.Integer(), nullable=False),
                    sa.Column('riserva', sa.String(length=1), nullable=True),
                    sa.Column('iscrizione', sa.String(length=7), nullable=True),
                    schema='ctcn'
                    )
    op.create_index('curiserv_idx1', 'curiserv', ['codice', 'sezione', 'immobile', 'tipo_imm', 'progressiv'],
                    schema='ctcn', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('curiserv_idx1', table_name='curiserv', schema='ctcn', postgresql_using='btree')
    op.drop_table('curiserv', schema='ctcn')
