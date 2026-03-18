# 🚀 Backend Production API

A production-ready REST API that handles user authentication and content management with scalable architecture and real-world backend practices.

---

## 📌 Overview

**Backend Production API** is a backend-focused project designed to simulate a real-world application backend:

* Handles user authentication with JWT
* Manages user-generated content (posts)
* Provides secure and protected endpoints
* Implements pagination and clean architecture
* Runs in a containerized environment and deployed to the cloud

This project demonstrates **backend engineering fundamentals**, including authentication, database design, API security, and deployment.

---

## 🧠 Key Features

### 🔹 Authentication System

* Secure user registration
* Password hashing using bcrypt
* JWT-based authentication
* Protected routes using Bearer tokens

---

### 🔹 User Management

* Create users via API
* Secure password storage
* Unique email validation

---

### 🔹 Posts System

* Full CRUD operations for posts
* Relationship between users and posts
* Auth-protected endpoints

---

### 🔹 API Features

* Pagination support for scalable data retrieval
* Clean service structure
* Modular FastAPI architecture

---

### 🔹 Production Setup

* Dockerized application
* Environment-based configuration
* Deployed to cloud platform

---

## 🏗️ Architecture

```
app/
├── api/            # Routes (FastAPI endpoints)
├── core/           # Config & security
├── db/             # Database setup, SQLAlchemy models
└── main.py         # App entry point
```

---

## ⚙️ Tech Stack

* **FastAPI** – high-performance web framework
* **PostgreSQL** – relational database
* **SQLAlchemy** – ORM
* **Alembic** – database migrations
* **APScheduler** – background job scheduling
* **Docker** – containerization
* **Render** – deployment

---

## 🔌 API Endpoints

### Auth

```
POST /api/v1/login
```

* Authenticate user and return JWT token

---

### Users

```
POST /api/v1/users
```

* Create new user

---

### Posts

```
GET /api/v1/posts
POST /api/v1/posts
GET /api/v1/posts/{id}
PUT /api/v1/posts/{id}
DELETE /api/v1/posts/{id}
```

* Full CRUD operations for posts

---

## 🔐 Authentication

Protected endpoints require:

```
Authorization: Bearer <your_token>
```

JWT tokens are generated upon login and used to access secured routes.

---

## 🐳 Running Locally

### 1. Clone the repository

```
git clone https://github.com/flobell/backend-production-api.git
cd backend-production-api
```

### 2. Configure environment variables

```
cp .env.example .env
```

### 3. Run with Docker

```
docker-compose up --build
```

---

### 3. Run manually

```
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

---

## 🌐 Deployment

The API is deployed on Render:

```
https://backend-production-api.onrender.com/docs
```

---

## 🎯 What This Project Demonstrates

This project highlights:

* Backend API design with authentication
* Secure password handling and JWT flows
* Relational database modeling
* RESTful API best practices
* Docker-based deployment
* Cloud deployment workflow

---

## 🚀 Future Improvements

* Role-based access control (RBAC)
* Rate limiting
* Logging & monitoring
* Unit and integration testing
* Caching layer (Redis)

---

## 👨‍💻 Author

**Pedro Flores**
Backend Developer (Python | FastAPI | PostgreSQL)

---

## ⭐ Why This Matters

This is not just a CRUD API.

It is a **production-style backend system** that reflects how real applications:

* authenticate users
* manage data securely
* structure scalable APIs
* deploy services to the cloud

---

👉 This project is part of my backend engineering portfolio focused on building production-ready systems.