from pydantic import BaseModel

class UnidadeBase(BaseModel):
    nome: str
    diretor: str

class UnidadeCreate(UnidadeBase):
    pass

class Unidade(UnidadeBase):
    id: int

    class Config:
        from_attributes = True
