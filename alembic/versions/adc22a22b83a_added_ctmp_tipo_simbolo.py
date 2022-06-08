"""Added ctmp.tipo_simbolo

Revision ID: adc22a22b83a
Revises: 2deec6474019
Create Date: 2022-06-08 08:25:25.940616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adc22a22b83a'
down_revision = '2deec6474019'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('tipo_simbolo',
                    sa.Column('codice', sa.Integer(), nullable=False,
                              comment='Codice del tipo di simobolo'),
                    sa.Column('descrizione', sa.String(length=100), nullable=True,
                              comment='Descrizione del tipo di simbolo'),
                    sa.PrimaryKeyConstraint('codice', name='tipo_simbolo_pkey'),
                    schema='ctmp',
                    comment='Descrizioni dei tipi di simbolo'
                    )


def downgrade() -> None:
    op.drop_table('tipo_simbolo', schema='ctmp')
