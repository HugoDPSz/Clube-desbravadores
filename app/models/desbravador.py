from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Desbravador(Base):
    __tablename__ = "desbravadores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    unidade_id = Column(Integer, ForeignKey("unidades.id"), nullable=False)

    unidade = relationship("Unidade")