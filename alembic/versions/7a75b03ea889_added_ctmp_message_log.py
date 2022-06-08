"""Added ctmp.message_log

Revision ID: 7a75b03ea889
Revises: 2507f2e1e507
Create Date: 2022-06-07 22:19:33.486854

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7a75b03ea889'
down_revision = '2507f2e1e507'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('message_log',
                    sa.Column('id', sa.BigInteger(), nullable=False,
                              comment='identificativo univoco del messaggio'),
                    sa.Column('log_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True,
                              comment='data e ora del messaggio'),
                    sa.Column('message', sa.Text(), nullable=True,
                              comment='messaggio'),
                    sa.PrimaryKeyConstraint('id', name='message_log_pkey'),
                    schema='ctmp',
                    comment='messaggi ed errori di tutte le procedure'
                    )
    op.create_index('message_log_idx1', 'message_log', ["log_time"],
                    schema='ctmp', postgresql_using='btree')
    op.create_index('message_log_idx2', 'message_log', ["message"],
                    schema='ctmp', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('message_log_idx1', table_name='message_log', schema='ctmp', postgresql_using='btree')
    op.drop_index('message_log_idx2', table_name='message_log', schema='ctmp', postgresql_using='btree')
    op.drop_table('message_log', schema='ctmp')
