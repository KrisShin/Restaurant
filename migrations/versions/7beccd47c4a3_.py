"""empty message

Revision ID: 7beccd47c4a3
Revises: 99636d780c76
Create Date: 2022-01-19 21:58:47.025377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7beccd47c4a3'
down_revision = '99636d780c76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_dish', sa.Column('discount_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tb_dish', 'tb_discount', ['discount_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tb_dish', type_='foreignkey')
    op.drop_column('tb_dish', 'discount_id')
    # ### end Alembic commands ###