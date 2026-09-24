import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200

def test_upload_missing_auth():
    res = client.post("/api/v1/documents", files={"file": ("test.pdf", b"pdfcontent", "application/pdf")})
    assert res.status_code == 403 or res.status_code == 401

def test_upload_invalid_type():
    token = str(uuid.uuid4())
    headers = {"Authorization": f"Bearer {token}"}
    res = client.post("/api/v1/documents", headers=headers, files={"file": ("test.exe", b"bad", "application/octet-stream")})
    assert res.status_code == 400
    assert res.json()["detail"]["code"] == "INVALID_FILE_TYPE"
