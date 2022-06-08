"""Added ctcn.ctqualit

Revision ID: 51bc73db4804
Revises: 7b86a96343e0
Create Date: 2022-06-07 15:06:36.555204

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '51bc73db4804'
down_revision = '7b86a96343e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('ctqualit',
                    sa.Column('codice', sa.Integer(), nullable=False, autoincrement=False),
                    sa.Column('qualita', sa.String(length=12), nullable=False),
                    sa.PrimaryKeyConstraint('codice', name='ctqualit_pkey'),
                    schema='ctcn'
                    )


def downgrade() -> None:
    op.drop_table('ctqualit', schema='ctcn')
