"""Add user model

Revision ID: cabdcfff54f9
Revises: edd697f38a3c
Create Date: 2023-09-01 14:20:36.387397

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'cabdcfff54f9'
down_revision = 'edd697f38a3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_create_date'), 'user', ['create_date'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_create_date'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
