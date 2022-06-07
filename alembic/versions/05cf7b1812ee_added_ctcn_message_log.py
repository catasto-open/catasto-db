"""Added ctcn.message_log

Revision ID: 05cf7b1812ee
Revises: ee3e7bb31b19
Create Date: 2022-06-07 17:08:38.233136

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import Sequence

revision = '05cf7b1812ee'
down_revision = 'ee3e7bb31b19'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('message_log',
                    sa.Column('id', sa.BigInteger(), nullable=False, comment='identificativo univoco del messaggio'),
                    sa.Column('log_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True,
                              comment='data e ora del messaggio'),
                    sa.Column('message', sa.Text(), nullable=True,
                              comment= 'messaggio'),
                    sa.PrimaryKeyConstraint('id', name='message_log_pkey'),
                    schema='ctcn',
                    comment='messaggi e errori di tutte le procedure'
                    )
    op.create_index('message_log_idx1', 'message_log', ['log_time'],
                    schema='ctcn', postgresql_using='btree')
    op.create_index('message_log_idx2', 'message_log', ['message'],
                    schema='ctcn', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('message_log_idx1', table_name='message_log', schema='ctcn', postgresql_using='btree')
    op.drop_index('message_log_idx2', table_name='message_log', schema='ctcn', postgresql_using='btree')
    op.drop_table('message_log', schema='ctcn')
