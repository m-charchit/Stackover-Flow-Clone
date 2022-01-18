"""empty message

Revision ID: b18ec9e3d44f
Revises: 411b1550a830
Create Date: 2021-07-08 23:49:50.726770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b18ec9e3d44f'
down_revision = '411b1550a830'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'question', 'detail', ['username'], ['username'])
    op.drop_column('question', 'user_username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('user_username', sa.VARCHAR(length=20), nullable=True))
    op.drop_constraint(None, 'question', type_='foreignkey')
    # ### end Alembic commands ###