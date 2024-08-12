from fastapi.testclient import TestClient
from main import app, SessionLocal, Base, engine
import pytest

# Initialize the test database
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client

def test_create_task(client):
    response = client.post("/tasks", json={"title": "New Task", "description": "This is a new task"})
    assert response.status_code == 200
    assert response.json()["title"] == "New Task"

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_task(client):
    task_id = client.get("/tasks").json()[0]["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

def test_delete_task(client):
    task_id = client.get("/tasks").json()[0]["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Task deleted successfully"
