"""Added ctcn.cttipnot

Revision ID: 228fb2ce24d3
Revises: 65619291306a
Create Date: 2022-06-07 15:32:08.289658

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '228fb2ce24d3'
down_revision = '65619291306a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('cttipnot',
                    sa.Column('tipo_nota', sa.String(length=1), nullable=False),
                    sa.Column('descrizion', sa.String(length=65), nullable=False),
                    sa.PrimaryKeyConstraint('tipo_nota', name="cttipnot_pkey"),
                    schema='ctcn'
                    )


def downgrade() -> None:
    op.drop_table('cttipnot', schema='ctcn')
