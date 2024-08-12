# Task Manager API

This project is a RESTful API built with FastAPI for managing tasks. It includes basic CRUD operations, persistent storage using SQLite, and automated testing with Pytest. The API is designed to be easily extensible, and it includes features such as searching and filtering.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [API Endpoints](#api-endpoints)
  - [Automated Tests](#automated-tests)
- [Database](#database)
- [Development](#development)


## Features

- Create, Read, Update, and Delete (CRUD) tasks.
- Persistent storage using SQLite.
- Search and filter tasks by title, status, and due date.
- Auto-generated API documentation with Swagger.
- Automated testing using Pytest.

## Requirements

- Python 3.8 or higher
- Pip package manager

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/irvinseet/task-manager-api.git
   cd task-manager-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the SQLite database**:
   The database will be automatically initialized when you first run the application.

## Usage

### Running the API

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### Task Endpoints

- **POST /tasks**: Create a new task.
- **GET /tasks**: Retrieve all tasks, with optional filtering by title, status, and due date.
- **GET /tasks/{task_id}**: Retrieve a specific task by its ID.
- **PUT /tasks/{task_id}**: Update an existing task by its ID.
- **DELETE /tasks/{task_id}**: Delete a task by its ID.

#### Auto-generated Documentation

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Automated Tests

To run the automated tests, use:

```bash
pytest
```

This will execute all the tests in `test_main.py` and provide a report of the test results.

## Database

The project uses SQLite for persistent storage. The database file is named `tasks.db` and is located in the project directory. The database schema is managed with SQLAlchemy, and the models are defined in `models.py`.

## Development

### Code Structure

- **`main.py`**: The main FastAPI application with route definitions.
- **`database.py`**: Database connection and setup.
- **`models.py`**: SQLAlchemy models for the database schema.
- **`test_main.py`**: Automated tests for the API.

