"""empty message

Revision ID: c94fca552609
Revises: 0fed0c6858a7
Create Date: 2020-03-16 17:03:53.684104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c94fca552609'
down_revision = '0fed0c6858a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('livematch',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('livematch')
    # ### end Alembic commands ###
