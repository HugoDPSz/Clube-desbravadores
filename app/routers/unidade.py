from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.unidade import UnidadeCreate, Unidade
from app.models.unidade import Unidade as UnidadeModel
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/unidades/", response_model=Unidade)
def criar_unidade(dados: UnidadeCreate, db: Session = Depends(get_db)):
    nova = UnidadeModel(**dados.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/unidades/", response_model=list[Unidade])
def listar_unidades(db: Session = Depends(get_db)):
    return db.query(UnidadeModel).all()