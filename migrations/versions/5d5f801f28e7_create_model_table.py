"""create model table

Revision ID: 5d5f801f28e7
Revises: 520aa6776347
Create Date: 2023-08-07 05:36:29.791610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5f801f28e7'
down_revision = '520aa6776347'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('end_point', sa.String(), nullable=False),
    sa.Column('model_provider_id', sa.Integer(), nullable=False),
    sa.Column('token_limit', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('version', sa.String(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('model_features', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('models')
    # ### end Alembic commands ###
