# StudyHub API

A backend REST API built using FastAPI and PostgreSQL for managing users and study tasks.
This project was developed as part of **DecodeLabs Full Stack Development – Project 3 (Database Integration)**. The main goal was to connect a backend application with a relational database, perform CRUD operations, and handle data reliably using proper schema design and validation. 

---

# Features

* User CRUD Operations
* Task CRUD Operations
* PostgreSQL Database Integration
* One-to-Many Relationships
* Input Validation with Pydantic
* Error Handling with HTTP Status Codes
* RESTful API Design
* Swagger API Documentation

---

# Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn

---

# Project Structure

```bash
Project-3/
│── app/
│   │── main.py
│   │── database.py
│   │── models.py
│   │── schemas.py
│   │── crud.py
│   │── routes.py
│
│── venv/
│── Public
│── .gitignore
│── requirements.txt
│── README.md
```

---

# Database Design

This project uses a relational database structure with a **One-to-Many** relationship.

### Relationship

* One User can have many Tasks
* One Task belongs to one User

### Tables

## Users Table

| Column | Type    |
| ------ | ------- |
| id     | Integer |
| name   | String  |
| email  | String  |

---

## Tasks Table

| Column  | Type        |
| ------- | ----------- |
| id      | Integer     |
| title   | String      |
| status  | String      |
| user_id | Foreign Key |

The project follows relational database concepts including:

* Primary Keys
* Foreign Keys
* CRUD Operations
* Proper Data Integrity 

---

# API Endpoints

## User Routes

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| POST   | `/users`            | Create a user       |
| GET    | `/users`            | Get all users       |
| GET    | `/users/{id}`       | Get single user     |
| GET    | `/users/{id}/tasks` | Get tasks of a user |
| GET    | `/users/{id}/full`  | Get user with tasks |

---

## Task Routes

| Method | Endpoint      | Description     |
| ------ | ------------- | --------------- |
| POST   | `/tasks`      | Create task     |
| GET    | `/tasks`      | Get all tasks   |
| GET    | `/tasks/{id}` | Get single task |
| PUT    | `/tasks/{id}` | Update task     |
| DELETE | `/tasks/{id}` | Delete task     |

---

# Validation & Error Handling

This project includes:

* Email validation
* Input length validation
* Duplicate email prevention
* User existence validation
* Proper HTTP status codes
* Database rollback handling

Example status codes used:

* `200` — Success
* `201` — Created
* `400` — Bad Request
* `404` — Not Found
* `422` — Validation Error

RESTful methods and proper status handling were an important part of the project requirements. 

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/sidd-sharma22/Decodelabs-FullStackDev.git
```

## 2. Open Project Folder

```bash
cd Decodelabs-FullStackDev\Project-3
```

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Setup PostgreSQL

Create database:

```sql
CREATE DATABASE studyhub_db;
```

## 6. Configure Environment Variables

Create `.env` file and add:

```env
DATABASE_URL=postgresql://postgres:my_password@localhost:5432/studyhub_db
```

## 7. Run Server

```bash
python -m uvicorn app.main:app --reload
```

---

# Swagger Documentation

After running the server:

### Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

# Example Request

## Create User

### POST `/users`

```json
{
  "name": "Sidd",
  "email": "sidd@gmail.com"
}
```

---

## Create Task

### POST `/tasks`

```json
{
  "title": "Learn PostgreSQL",
  "status": "Pending",
  "user_id": 1
}
```

---

# Learning Outcomes

This project helped in understanding:

* Database Integration
* Relational Database Design
* CRUD Operations
* REST APIs
* SQLAlchemy ORM
* Schema Validation
* Error Handling
* PostgreSQL Integration
* Backend Architecture

Project 3 mainly focused on connecting backend logic with permanent data storage using schema design and CRUD operations. 

---

# Future Improvements

* JWT Authentication
* Role-Based Access
* Alembic Migrations
* Pagination
* Search & Filtering
* Docker Support
* Unit Testing

---

# Acknowledgement

This project was developed as part of the DecodeLabs Full Stack Development Internship Program. 

---

# Author

Siddharth Sharma  
CSE Student | Full Stack Development Intern - DecodeLabs