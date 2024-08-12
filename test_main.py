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
    # Create a task first
    create_response = client.post("/tasks", json={"title": "Task to Update", "description": "Update this task"})
    task_id = create_response.json()["id"]
    
    # Update the task
    update_response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "description": "This task has been updated"})
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Task"

def test_delete_task(client):
    # Create a task first
    create_response = client.post("/tasks", json={"title": "Task to Delete", "description": "Delete this task"})
    task_id = create_response.json()["id"]
    
    # Delete the task
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["detail"] == "Task deleted successfully"
