from pydantic import BaseModel
from typing import Optional

class DesbravadorCreate(BaseModel):
    nome: str
    idade: int
    unidade_id: str

class DesbravadorComUnidade(DesbravadorCreate):
    unidade_nome: Optional[str]
