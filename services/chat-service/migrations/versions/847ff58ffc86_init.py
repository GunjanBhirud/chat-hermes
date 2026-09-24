"""init

Revision ID: 847ff58ffc86
Revises: 
Create Date: 2026-09-24 13:05:59.814375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '847ff58ffc86'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('conversations',
    sa.Column('id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('owner_id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('document_ids', sa.ARRAY(sa.UUID(as_uuid=True)), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('conversation_id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('source_chunk_ids', sa.ARRAY(sa.UUID(as_uuid=True)), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('messages')
    op.drop_table('conversations')
