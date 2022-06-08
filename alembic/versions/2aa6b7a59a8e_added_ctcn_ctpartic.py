"""Added ctcn.ctpartic

Revision ID: 2aa6b7a59a8e
Revises: d1255e68d0bb
Create Date: 2022-06-07 14:30:53.862314

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2aa6b7a59a8e'
down_revision = 'd1255e68d0bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('ctpartic',
                    sa.Column('codice', sa.String(length=4), nullable=False),
                    sa.Column('sezione', sa.String(length=1), nullable=False),
                    sa.Column('immobile', sa.BigInteger(), nullable=False),
                    sa.Column('tipo_imm', sa.String(length=1), nullable=False),
                    sa.Column('progressiv', sa.Integer(), nullable=False),
                    sa.Column('foglio', sa.Integer(), nullable=True),
                    sa.Column('numero', sa.String(length=5), nullable=True),
                    sa.Column('denominato', sa.Integer(), nullable=True),
                    sa.Column('subalterno', sa.String(length=4), nullable=True),
                    sa.Column('edificiale', sa.String(length=1), nullable=True),
                    sa.Column('qualita', sa.Integer(), nullable=True),
                    sa.Column('classe', sa.String(length=2), nullable=True),
                    sa.Column('ettari', sa.Integer(), nullable=True),
                    sa.Column('are', sa.Integer(), nullable=True),
                    sa.Column('centiare', sa.Integer(), nullable=True),
                    sa.Column('flag_redd', sa.String(length=1), nullable=True),
                    sa.Column('flag_porz', sa.String(length=1), nullable=True),
                    sa.Column('flag_deduz', sa.String(length=1), nullable=True),
                    sa.Column('dominic_l', sa.String(length=9), nullable=True),
                    sa.Column('agrario_l', sa.String(length=8), nullable=True),
                    sa.Column('dominic_e', sa.String(length=12), nullable=True),
                    sa.Column('agrario_e', sa.String(length=11), nullable=True),
                    sa.Column('gen_eff', sa.String(length=10), nullable=True),
                    sa.Column('gen_regist', sa.String(length=10), nullable=True),
                    sa.Column('gen_tipo', sa.String(length=1), nullable=True),
                    sa.Column('gen_numero', sa.String(length=6), nullable=True),
                    sa.Column('gen_progre', sa.String(length=3), nullable=True),
                    sa.Column('gen_anno', sa.Integer(), nullable=True),
                    sa.Column('con_eff', sa.String(length=10), nullable=True),
                    sa.Column('con_regist', sa.String(length=10), nullable=True),
                    sa.Column('con_tipo', sa.String(length=1), nullable=True),
                    sa.Column('con_numero', sa.String(length=6), nullable=True),
                    sa.Column('con_progre', sa.String(length=3), nullable=True),
                    sa.Column('con_anno', sa.Integer(), nullable=True),
                    sa.Column('partita', sa.String(length=7), nullable=True),
                    sa.Column('annotazion', sa.String(length=200), nullable=True),
                    sa.Column('mutaz_iniz', sa.Integer(), nullable=True),
                    sa.Column('mutaz_fine', sa.Integer(), nullable=True),
                    sa.Column('gen_causa', sa.String(length=3), nullable=True),
                    sa.Column('gen_descr', sa.String(length=100), nullable=True),
                    sa.Column('con_causa', sa.String(length=3), nullable=True),
                    sa.Column('con_descr', sa.String(length=100), nullable=True),
                    sa.PrimaryKeyConstraint('codice', 'sezione', 'immobile', 'tipo_imm', 'progressiv',
                                            name='ctpartic_pkey'),
                    schema='ctcn'
                    )
    op.create_index('ctpartic_idx1', 'ctpartic', ["codice", "sezione", "foglio", "numero"],
                    schema='ctcn', postgresql_using='btree')


def downgrade() -> None:
    op.drop_index('ctpartic_idx1', table_name='ctpartic', schema='ctcn', postgresql_using='btree')
    op.drop_table('ctpartic', schema='ctcn')
