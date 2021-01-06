"""initial

Revision ID: 31d8acda6998
Revises:
Create Date: 2020-05-17 00:40:22.177633

"""
from alembic import op
import sqlalchemy as sa
import alvinchow_service.db.types
from alvinchow_service.db.types import Text   # this is just for custom JSONB Alembic bug, remove if not needed


# revision identifiers, used by Alembic.
revision = '31d8acda6998'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_next_bigint_id_function()
    op.create_table('user',
    sa.Column('created_at', alvinchow_service.db.types.UTCDateTime(timezone=True), nullable=True),
    sa.Column('updated_at', alvinchow_service.db.types.UTCDateTime(timezone=True), nullable=True),
    sa.Column('id', alvinchow_service.db.types.BigIntegerID(), nullable=False),
    sa.Column('username', alvinchow_service.db.types.Text(), nullable=True),
    sa.Column('email', alvinchow_service.db.types.Text(), nullable=True),
    sa.Column('password', alvinchow_service.db.types.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.execute('ALTER TABLE "user" ALTER COLUMN id set default next_bigint_id(\'user_id_seq\')')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_next_bigint_id_function()
    # ### end Alembic commands ###
