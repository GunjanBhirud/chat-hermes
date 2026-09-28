import asyncio
import uuid
import sys
sys.path.append('.')
from app.db.session import AsyncSessionLocal
from app.ingestion.processor import process_document
from app.config import settings

async def main():
    async with AsyncSessionLocal() as session:
        await process_document(uuid.UUID("ede59ded-5d89-46dd-8a4c-f96fda313258"), session)

asyncio.run(main())
