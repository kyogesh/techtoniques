"""empty message

Revision ID: 018e23b96464
Revises: 
Create Date: 2020-02-28 12:58:20.887314

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '018e23b96464'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('house_num', sa.Integer(), nullable=True),
    sa.Column('street', sa.String(length=100, _expect_unicode=True), nullable=True),
    sa.Column('locality', sa.String(length=100, _expect_unicode=True), nullable=True),
    sa.Column('city', sa.String(length=100, _expect_unicode=True), nullable=True),
    sa.Column('state', sa.String(length=100, _expect_unicode=True), nullable=True),
    sa.Column('pincode', sa.Integer(), nullable=True),
    sa.Column('present', sa.Boolean()),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100, _expect_unicode=True), nullable=True),
    sa.Column('last_name', sa.String(length=100, _expect_unicode=True), nullable=True),
    sa.Column('email', sa.String(length=255, _expect_unicode=True), nullable=True),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(length=1137), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('addresses')
    # ### end Alembic commands ###