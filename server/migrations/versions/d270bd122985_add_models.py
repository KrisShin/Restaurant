"""add models

Revision ID: d270bd122985
Revises: 
Create Date: 2021-01-14 19:13:45.429189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd270bd122985'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_dish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('discount_type', sa.Integer(), nullable=True),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=128), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('avatar', sa.String(length=512), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('gender', sa.Boolean(), nullable=True),
    sa.Column('role', sa.Enum('user', 'admin', name='role_enum'), nullable=True),
    sa.Column('is_new', sa.Boolean(), nullable=True),
    sa.Column('is_vip', sa.Boolean(), nullable=True),
    sa.Column('is_actice', sa.Boolean(), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('tb_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('location', sa.String(length=512), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('money', sa.Float(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('note', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['tb_address.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=512), nullable=True),
    sa.Column('rate', sa.Enum('good', 'ok', 'bad', name='rate_enum'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['tb_order.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_comment')
    op.drop_table('tb_order')
    op.drop_table('tb_address')
    op.drop_table('tb_user')
    op.drop_table('tb_tag')
    op.drop_table('tb_dish')
    # ### end Alembic commands ###