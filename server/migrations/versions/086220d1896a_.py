"""empty message

Revision ID: 086220d1896a
Revises: 6c1d8714bfb0
Create Date: 2021-03-10 16:10:24.642862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '086220d1896a'
down_revision = '6c1d8714bfb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('update_time1', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'update_time1')
    # ### end Alembic commands ###
