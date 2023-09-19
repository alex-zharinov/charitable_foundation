"""Fix Donation and Proj

Revision ID: e10d631cb8b2
Revises: 98555a98b475
Create Date: 2023-09-04 12:27:04.432835

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'e10d631cb8b2'
down_revision = '98555a98b475'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charityproject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_charityproject_create_date'), 'charityproject', ['create_date'], unique=False)
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_donation_create_date'), 'donation', ['create_date'], unique=False)
    op.drop_index('ix_user_email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=320), nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.drop_index(op.f('ix_donation_create_date'), table_name='donation')
    op.drop_table('donation')
    op.drop_index(op.f('ix_charityproject_create_date'), table_name='charityproject')
    op.drop_table('charityproject')
    # ### end Alembic commands ###