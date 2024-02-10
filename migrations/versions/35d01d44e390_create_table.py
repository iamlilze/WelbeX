"""create table

Revision ID: 35d01d44e390
Revises:
Create Date: 2024-02-06 13:05:43.278749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35d01d44e390'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'routes',
        sa.Column('id', sa.Integer, primary_key=True, index=True)
    )
    op.create_table(
        'points',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('lat', sa.Float),
        sa.Column('lng', sa.Float),
        sa.Column('route_id', sa.Integer, sa.ForeignKey('routes.id'))
    )
