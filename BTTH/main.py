from fastapi import FastAPI
from database import engine, Base
import models.user
from routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="JWT Authentication Modular")

app.include_router(auth.router)