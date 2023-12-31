"""Fix User model

Revision ID: 98555a98b475
Revises: cabdcfff54f9
Create Date: 2023-09-01 14:36:56.076399

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '98555a98b475'
down_revision = 'cabdcfff54f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_charityproject_create_date', table_name='charityproject')
    op.drop_table('charityproject')
    op.drop_index('ix_donation_create_date', table_name='donation')
    op.drop_table('donation')
    op.drop_index('ix_user_create_date', table_name='user')
    op.drop_column('user', 'fully_invested')
    op.drop_column('user', 'invested_amount')
    op.drop_column('user', 'close_date')
    op.drop_column('user', 'full_amount')
    op.drop_column('user', 'create_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_date', sa.DATETIME(), nullable=True))
    op.add_column('user', sa.Column('full_amount', sa.INTEGER(), nullable=False))
    op.add_column('user', sa.Column('close_date', sa.DATETIME(), nullable=True))
    op.add_column('user', sa.Column('invested_amount', sa.INTEGER(), nullable=True))
    op.add_column('user', sa.Column('fully_invested', sa.BOOLEAN(), nullable=True))
    op.create_index('ix_user_create_date', 'user', ['create_date'], unique=False)
    op.create_table('donation',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('full_amount', sa.INTEGER(), nullable=False),
    sa.Column('fully_invested', sa.BOOLEAN(), nullable=True),
    sa.Column('invested_amount', sa.INTEGER(), nullable=True),
    sa.Column('create_date', sa.DATETIME(), nullable=True),
    sa.Column('close_date', sa.DATETIME(), nullable=True),
    sa.Column('comment', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_donation_create_date', 'donation', ['create_date'], unique=False)
    op.create_table('charityproject',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('full_amount', sa.INTEGER(), nullable=False),
    sa.Column('fully_invested', sa.BOOLEAN(), nullable=True),
    sa.Column('create_date', sa.DATETIME(), nullable=True),
    sa.Column('close_date', sa.DATETIME(), nullable=True),
    sa.Column('invested_amount', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index('ix_charityproject_create_date', 'charityproject', ['create_date'], unique=False)
    # ### end Alembic commands ###
