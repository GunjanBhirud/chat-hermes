import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote_plus

class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5433/document_chat"
    storage_path: str = "/tmp/documents"
    max_file_size_mb: int = 50
    embedding_provider: str = "openrouter"
    embedding_base_url: str = "https://openrouter.ai/api/v1"
    embedding_model: str = "text-embedding-ada-002"
    embedding_api_key: str = ""
    embedding_dimensions: int = 1536
    chunk_size: int = 900
    chunk_overlap: int = 120

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

os.makedirs(settings.storage_path, exist_ok=True)
