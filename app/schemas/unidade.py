from pydantic import BaseModel, Field
from typing import Optional

class UnidadeBase(BaseModel):
    nome: str
    diretor: str

class UnidadeCreate(UnidadeBase):
    pass 

class Unidade(UnidadeBase):
    id: str = Field(alias= "_id")