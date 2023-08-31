"""Renaming students to scholars

Revision ID: b9d342df2e6a
Revises: 791279dd0760
Create Date: 2023-08-31 21:33:31.470679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9d342df2e6a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
