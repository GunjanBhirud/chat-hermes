import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200

def test_create_conversation_unauth():
    payload = {"document_ids": [str(uuid.uuid4())], "title": "Test Auth"}
    res = client.post("/api/v1/conversations", json=payload)
    assert res.status_code == 403 or res.status_code == 401

def test_fetch_conversation_unauth():
    res = client.get(f"/api/v1/conversations/{uuid.uuid4()}")
    assert res.status_code == 403 or res.status_code == 401
