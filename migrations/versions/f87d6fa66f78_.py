"""empty message

Revision ID: f87d6fa66f78
Revises: 17d30965bd4a
Create Date: 2021-11-21 12:59:39.989207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f87d6fa66f78'
down_revision = '17d30965bd4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('rate', sa.Enum('good', 'ok', 'bad', name='rate_enum'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'rate')
    # ### end Alembic commands ###
