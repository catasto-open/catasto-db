"""Added ctcn.ctriserv

Revision ID: 65619291306a
Revises: 51bc73db4804
Create Date: 2022-06-07 15:21:31.678446

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '65619291306a'
down_revision = '51bc73db4804'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('ctriserv',
                    sa.Column('codice', sa.String(length=4), nullable=False),
                    sa.Column('sezione', sa.String(length=1), nullable=False),
                    sa.Column('immobile', sa.BigInteger(), nullable=False),
                    sa.Column('tipo_imm', sa.String(length=1), nullable=False),
                    sa.Column('progressiv', sa.Integer(), nullable=False),
                    sa.Column('riserva', sa.String(length=1), nullable=True),
                    sa.Column('iscrizione', sa.String(length=7), nullable=True),
                    schema='ctcn'
                    )
    op.create_index('ctriserv_idx1', 'ctriserv', ["codice", "sezione", "immobile", "tipo_imm", "progressiv"],
                    schema='ctcn', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('ctriserv_idx1', table_name='ctriserv', schema='ctcn', postgresql_using='btree')
    op.drop_table('ctriserv', schema='ctcn')
