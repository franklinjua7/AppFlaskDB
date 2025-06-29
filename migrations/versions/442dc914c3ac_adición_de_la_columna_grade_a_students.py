"""Adición de la columna grade a Students

Revision ID: 442dc914c3ac
Revises: 
Create Date: 2025-06-18 08:24:51.034858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '442dc914c3ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grade', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_column('grade')

    # ### end Alembic commands ###
