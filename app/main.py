from fastapi import FastAPI
from app.routers import desbravador, unidade

app = FastAPI()
app.include_router(unidade.router, prefix="/api", tags=["Unidades"])
app.include_router(desbravador.router, prefix="/api", tags=["Desbravadores"])

from app.database import Base, engine
from app.models import desbravador, unidade

Base.metadata.create_all(bind=engine)
