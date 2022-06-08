"""Added ctcn.esteri

Revision ID: ee3e7bb31b19
Revises: 3241a81a8849
Create Date: 2022-06-07 17:01:46.015304

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ee3e7bb31b19'
down_revision = '3241a81a8849'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('esteri',
                    sa.Column('codice', sa.String(length=4), nullable=False),
                    sa.Column('sigla', sa.String(length=4), nullable=True),
                    sa.Column('denominaz', sa.String(length=65), nullable=False),
                    sa.PrimaryKeyConstraint('codice', name='esteri_pkey'),
                    schema='ctcn'
                    )


def downgrade() -> None:
    op.drop_table('esteri', schema='ctcn')
