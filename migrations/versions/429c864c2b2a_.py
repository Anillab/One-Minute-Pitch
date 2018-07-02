"""empty message

Revision ID: 429c864c2b2a
Revises: 7afcfbbdc121
Create Date: 2018-07-02 11:55:06.897244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '429c864c2b2a'
down_revision = '7afcfbbdc121'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_of_category', sa.String(length=255), nullable=True),
    sa.Column('category_description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pitch_categories')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch_categories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name_of_category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('category_description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pitch_categories_pkey')
    )
    op.drop_table('categories')
    # ### end Alembic commands ###