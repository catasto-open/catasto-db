"""Added ctcn.ctnonfis

Revision ID: d1255e68d0bb
Revises: 5899db015043
Create Date: 2022-06-07 14:17:37.849911

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = 'd1255e68d0bb'
down_revision = '5899db015043'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('ctnonfis',
                    sa.Column('codice', sa.String(length=4), nullable=False),
                    sa.Column('sezione', sa.String(length=1), nullable=False),
                    sa.Column('soggetto', sa.BigInteger(), nullable=False),
                    sa.Column('tipo_sog', sa.String(length=1), nullable=False),
                    sa.Column('denominaz', sa.String(length=150), nullable=True),
                    sa.Column('sede', sa.String(length=4), nullable=True),
                    sa.Column('codfiscale', sa.String(length=11), nullable=True),
                    sa.PrimaryKeyConstraint('codice', 'sezione', 'soggetto', 'tipo_sog', name='ctnonfis_pkey'),
                    schema='ctcn'
                    )
    op.create_index('ctnonfis_i1', 'ctnonfis', [text("denominaz varchar_pattern_ops")],
                    schema='ctcn', postgresql_using='btree')
    op.create_index('ctnonfis_i2', 'ctnonfis', [text("codfiscale varchar_pattern_ops")],
                    schema='ctcn', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('ctnonfis_i1', table_name='ctnonfis', schema='ctcn', postgresql_using='btree')
    op.drop_index('ctnonfis_i2', table_name='ctnonfis', schema='ctcn', postgresql_using='btree')
    op.drop_table('ctnonfis', schema='ctcn')
