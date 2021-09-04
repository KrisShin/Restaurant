"""empty message

Revision ID: 25e3b7c748e6
Revises: 8548f3c84490
Create Date: 2021-05-08 23:58:27.450544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25e3b7c748e6'
down_revision = '8548f3c84490'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('rate', sa.Enum('good', 'ok', 'bad', name='rate_enum'), nullable=True))
    op.add_column('user', sa.Column('role', sa.Enum('user', 'admin', name='role_enum'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    op.drop_column('comment', 'rate')
    # ### end Alembic commands ###