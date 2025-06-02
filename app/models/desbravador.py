from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Desbravador(Base):
    __tablename__ = "desbravadores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    unidade = Column(String)