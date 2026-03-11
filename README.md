# FastAPI Backend Portfolio Project

Backend API built with FastAPI, PostgreSQL and Docker.

## Features

- JWT Authentication
- User registration and login
- Posts CRUD
- Authorization (users can only modify their own posts)
- Pagination support
- PostgreSQL database
- Dockerized environment

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- JWT

## Run the project

Clone the repository:

```bash
git clone <repo_url>
cd <repo>
```

Start the project:
```bash
docker-compose up --build
```

The API will be available at:
```bash
http://localhost:8000/docs
```

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

