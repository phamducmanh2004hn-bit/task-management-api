# Task Management API

A basic RESTful API for managing users and tasks, built with Python and FastAPI.

## Tech Stack

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* SQLite
* Alembic
* Uvicorn

## Features

### User Management

* Create a user
* Get all users
* Get a user by ID
* Update a user
* Delete a user
* Get all tasks belonging to a user

### Task Management

* Create a task
* Get all tasks
* Get a task by ID
* Update a task
* Delete a task
* Assign a task to a user

### Validation & Error Handling

* Request validation with Pydantic
* Email validation with `EmailStr`
* Field length validation
* Task status validation
* `404 Not Found` handling for missing users and tasks

## Project Structure

```text
task-management-api/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │
│   ├── crud/
│   │   ├── task.py
│   │   └── user.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── database.py
│   │   └── deps.py
│   │
│   ├── models/
│   │   ├── task.py
│   │   └── user.py
│   │
│   ├── router/
│   │   ├── task.py
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── task.py
│   │   └── user.py
│   │
│   └── main.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── tests/
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

## Database Relationship

The project uses a one-to-many relationship:

```text
User
  │
  └───< Task
```

One user can have multiple tasks, while each task belongs to one user.

## API Endpoints

### User

| Method | Endpoint                | Description         |
| ------ | ----------------------- | ------------------- |
| GET    | `/user/`                | Get all users       |
| GET    | `/user/{user_id}`       | Get a user by ID    |
| GET    | `/user/{user_id}/tasks` | Get tasks of a user |
| POST   | `/user/`                | Create a user       |
| PUT    | `/user/{user_id}`       | Update a user       |
| DELETE | `/user/{user_id}`       | Delete a user       |

### Task

| Method | Endpoint          | Description      |
| ------ | ----------------- | ---------------- |
| GET    | `/task/`          | Get all tasks    |
| GET    | `/task/{task_id}` | Get a task by ID |
| POST   | `/task/`          | Create a task    |
| PUT    | `/task/{task_id}` | Update a task    |
| DELETE | `/task/{task_id}` | Delete a task    |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/phamducmanh2004hn-bit/task-management-api.git
cd task-management-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
alembic upgrade head
```

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI Swagger UI can be used to test all available endpoints.

## Project Scope

This project focuses on the core concepts of a FastAPI backend application:

* REST API
* CRUD operations
* Pydantic schemas
* SQLAlchemy ORM
* Database relationships
* Alembic migrations
* Request validation
* Basic error handling

Authentication and JWT are intentionally outside the scope of this basic version.

## Status

Basic version completed.
