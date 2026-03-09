import json
from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_add_task():
    response = client.post("/tasks",
        json={"title": "Test Task"}
    )
    assert response.status_code == 201

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
