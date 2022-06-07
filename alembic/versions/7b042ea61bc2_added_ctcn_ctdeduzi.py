"""Added ctcn.ctdeduzi

Revision ID: 7b042ea61bc2
Revises: 0b3dc6b9ed65
Create Date: 2022-06-07 13:33:07.533215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b042ea61bc2'
down_revision = '0b3dc6b9ed65'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('ctdeduzi',
                    sa.Column('codice', sa.String(length=4), nullable=False),
                    sa.Column('sezione', sa.String(length=1), nullable=False),
                    sa.Column('immobile', sa.BigInteger(), nullable=False),
                    sa.Column('tipo_imm', sa.String(length=1), nullable=False),
                    sa.Column('progressiv', sa.Integer(), nullable=False),
                    sa.Column('deduzione', sa.String(length=6), nullable=True),
                    schema='ctcn'
                    )
    op.create_index('ctdeduzi_idx1', 'ctdeduzi', ['codice', 'sezione', 'immobile', 'tipo_imm', 'progressiv'],
                    schema='ctcn', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('ctdeduzi_idx1', table_name='ctdeduzi', schema='ctcn', postgresql_using='btree')
    op.drop_table('ctdeduzi', schema='ctcn')
