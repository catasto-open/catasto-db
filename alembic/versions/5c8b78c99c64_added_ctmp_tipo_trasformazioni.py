"""Added ctmp.tipo_trasformazioni

Revision ID: 5c8b78c99c64
Revises: adc22a22b83a
Create Date: 2022-06-08 08:26:17.622203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c8b78c99c64'
down_revision = 'adc22a22b83a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('tipo_trasformazioni',
                    sa.Column('codice', sa.String(length=20), nullable=False,
                              comment='Codice del tipo di trasformazione'),
                    sa.Column('descrizione', sa.String(length=1000), nullable=False,
                              comment='Descrizione del tipo di trasformazione'),
                    sa.PrimaryKeyConstraint('codice', name='tipo_trasformazioni_pkey'),
                    schema='ctmp',
                    comment='Tipologie di trasformazioni geometriche'
                    )


def downgrade() -> None:
    op.drop_table('tipo_trasformazioni', schema='ctmp')
