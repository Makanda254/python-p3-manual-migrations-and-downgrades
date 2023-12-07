"""Renaming students to graduates

Revision ID: c83fe827622e
Revises: 791279dd0760
Create Date: 2023-12-07 22:23:15.017353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c83fe827622e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'graduates')

  


def downgrade() -> None:
    op.rename_table('graduates', 'students')
    
