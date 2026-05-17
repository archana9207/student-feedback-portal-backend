# Student Feedback Portal - Backend

A RESTful backend API for the Student Feedback Portal built using Django, Django REST Framework, PostgreSQL, and JWT Authentication.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Simple JWT

---

## Features

- User Registration
- User Login with JWT Authentication
- Refresh Token Authentication
- Authenticated user profile 
- Ownership-based permissions
- Feedback CRUD Operations
- Protected APIs
- PostgreSQL Database Integration
- Class-Based Views
- RESTful API Architecture

---

## Project Structure

```plaintext
backend/
│
├── apps/
│   ├── authentication/
│   └── feedback/
│
├── core/
├── requirements.txt
├── .env
└── manage.py
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/archana9207/student-feedback-portal-backend.git
cd backend
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside backend directory:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=student_feedback_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Database Setup

Create PostgreSQL database:

```plaintext
student_feedback_db
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run Server

```bash
python manage.py runserver
```

Backend Server:

```plaintext
http://127.0.0.1:8000
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register user |
| POST | `/api/auth/login/` | Login user |
| POST | `/api/auth/refresh/` | Refresh JWT token |
| GET | `/api/auth/profile/` | Get authenticated user profile |
| PATCH | `/api/auth/profile/` | Update profile  |

---

### Feedback APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/feedbacks/` | Get all feedbacks |
| POST | `/api/feedbacks/` | Create feedback |
| GET | `/api/feedbacks/<id>/` | Get single feedback |
| PUT | `/api/feedbacks/<id>/` | Update feedback |
| DELETE | `/api/feedbacks/<id>/` | Delete feedback |

---

## Authentication

Protected APIs require JWT access token.

Example:

```http
Authorization: Bearer your_access_token
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

Admin Panel:

```plaintext
http://127.0.0.1:8000/admin
```

---

## Requirements

Generate requirements file:

```bash
pip freeze > requirements.txt
```

---

## Author

Archana K