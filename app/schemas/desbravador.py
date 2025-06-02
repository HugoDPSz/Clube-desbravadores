from pydantic import BaseModel, Field
from typing import Optional

class DesbravadorBase(BaseModel):
    nome: str
    idade: int
    unidade: str

class DesbravadorCreate(DesbravadorBase):
    pass

class Desbravador(DesbravadorBase):
    id: str = Field(alias="_id")