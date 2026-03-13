# Backend Production API

A production-style REST API built with FastAPI.

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Docker
- Render (cloud deployment)

## Features

- User registration
- JWT authentication
- Posts CRUD
- Pagination
- Database migrations
- Dockerized deployment
- OpenAPI documentation

## Live API

Swagger documentation:

https://backend-production-api.onrender.com/docs

## Local Setup

Clone the repository:

git clone https://github.com/yourusername/backend-production-api.git

Install dependencies:

pip install -r requirements.txt

Run the API:

uvicorn app.main:app --reload

## Docker

docker compose up --build -d

## API Endpoints
### Auth
- POST /api/v1/login
### Users
- GET /api/v1/users
- POST /api/v1/users
- GET /api/v1/users/me
### Posts
- POST /api/v1/posts
- GET /api/v1/posts (Supports pagination)
    - GET ../api/v1/posts?skip=0&limit=10
- GET /api/v1/posts/{id}
- PUT /api/v1/posts/{id}
- DELETE /api/v1/posts/{id}

