"""init

Revision ID: b1ce42c5bdca
Revises: 
Create Date: 2026-09-24 12:23:21.559453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1ce42c5bdca'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    op.create_table('documents',
    sa.Column('id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('owner_id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('original_filename', sa.String(), nullable=False),
    sa.Column('mime_type', sa.String(), nullable=False),
    sa.Column('file_size', sa.BigInteger(), nullable=False),
    sa.Column('storage_key', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('error_code', sa.String(), nullable=True),
    sa.Column('error_message', sa.String(), nullable=True),
    sa.Column('page_count', sa.Integer(), nullable=True),
    sa.Column('chunk_count', sa.Integer(), nullable=True),
    sa.Column('embedding_model', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('processed_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('document_chunks',
    sa.Column('id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('document_id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('owner_id', sa.UUID(as_uuid=True), nullable=False),
    sa.Column('chunk_index', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('embedding', sa.String(), nullable=True),
    sa.Column('page_start', sa.Integer(), nullable=True),
    sa.Column('page_end', sa.Integer(), nullable=True),
    sa.Column('heading_path_text', sa.String(), nullable=True),
    sa.Column('source_metadata_text', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['document_id'], ['documents.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.execute("ALTER TABLE document_chunks ALTER COLUMN embedding TYPE vector(1024) USING (embedding::vector);")

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('document_chunks')
    op.drop_table('documents')
