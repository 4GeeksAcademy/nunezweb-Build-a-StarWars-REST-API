"""empty message

Revision ID: 10c90d4c5e15
Revises: 47e1bf3169c0
Create Date: 2024-07-23 23:24:34.186710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10c90d4c5e15'
down_revision = '47e1bf3169c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('climate',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('terrain',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('terrain',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('climate',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
