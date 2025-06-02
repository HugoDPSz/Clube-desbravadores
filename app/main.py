from fastapi import FastAPI
from app.routers import desbravador

app = FastAPI()
app.include_router(desbravador.router, prefix="/api")