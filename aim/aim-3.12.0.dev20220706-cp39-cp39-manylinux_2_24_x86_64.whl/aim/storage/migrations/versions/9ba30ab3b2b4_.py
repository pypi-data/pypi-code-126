"""empty message

Revision ID: 9ba30ab3b2b4
Revises: fbfe5c4702fb
Create Date: 2021-08-27 18:17:27.819214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ba30ab3b2b4'
down_revision = 'fbfe5c4702fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tag', 'description')
    # ### end Alembic commands ###
