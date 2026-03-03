from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.db.models import user  # importante importar el modelo
from app.api.v1.endpoints import users

Base.metadata.create_all(bind=engine)
# print("Database tables created successfully.")

app = FastAPI()
app.include_router(users.router, prefix="/api/v1", tags=["users"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def read_health():
    return {"status": "ok"}
