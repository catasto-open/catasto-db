"""Added ctcn.cuptaspe

Revision ID: e3f49243636f
Revises: a843bb3ee075
Create Date: 2022-06-07 16:47:27.443604

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e3f49243636f'
down_revision = 'a843bb3ee075'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('cuptaspe',
                    sa.Column('partita', sa.String(length=1), nullable=False),
                    sa.Column('descrizion', sa.String(length=100), nullable=False),
                    sa.PrimaryKeyConstraint('partita', name='cuptaspe_pkey'),
                    schema='ctcn'
                    )


def downgrade() -> None:
    op.drop_table('cuptaspe', schema='ctcn')
