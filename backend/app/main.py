import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router

app = FastAPI()

_raw_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000")
origins = [o.strip() for o in _raw_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(api_router)