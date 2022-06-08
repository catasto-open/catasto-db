"""Added ctcn.ctptaspe

Revision ID: 7b86a96343e0
Revises: fd5aaca95861
Create Date: 2022-06-07 15:00:24.655362

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7b86a96343e0'
down_revision = 'fd5aaca95861'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('ctptaspe',
                    sa.Column('partita', sa.String(length=1), nullable=False),
                    sa.Column('descrizion', sa.String(length=100), nullable=False),
                    sa.PrimaryKeyConstraint('partita', name='ctptaspe_pkey'),
                    schema='ctcn'
                    )


def downgrade() -> None:
    op.drop_table('ctptaspe', schema='ctcn')
