import os
import uuid
import shutil
from fastapi import UploadFile
from ..config import settings

def save_upload_file(upload_file: UploadFile, doc_id: uuid.UUID) -> str:
    ext = upload_file.filename.split('.')[-1].lower() if upload_file.filename else 'bin'
    storage_key = f"{doc_id}.{ext}"
    dest_path = os.path.join(settings.storage_path, storage_key)
    
    upload_file.file.seek(0)
    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
        
    return storage_key

def delete_file(storage_key: str) -> None:
    dest_path = os.path.join(settings.storage_path, storage_key)
    if os.path.exists(dest_path):
        os.remove(dest_path)
