from fastapi import FastAPI
from app.routers import desbravador
from app.routers import unidade

app = FastAPI()
app.include_router(desbravador.router, prefix="/api")
app.include_router(unidade.router, prefix="/api")