from pydantic import BaseModel
from app.schemas.unidade import Unidade

class DesbravadorBase(BaseModel):
    nome: str
    idade: int
    unidade_id: int

class DesbravadorCreate(DesbravadorBase):
    pass

class Desbravador(BaseModel):
    id: int
    nome: str
    idade: int
    unidade: Unidade  # Aqui entra o JOIN

    class Config:
        from_attributes = True