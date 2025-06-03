from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.desbravador import DesbravadorCreate, Desbravador
from app.models.desbravador import Desbravador as DesbravadorModel
from app.models.unidade import Unidade as UnidadeModel
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/desbravadores/", response_model=Desbravador)
def criar_desbravador(dados: DesbravadorCreate, db: Session = Depends(get_db)):
    unidade = db.query(UnidadeModel).filter(UnidadeModel.id == dados.unidade_id).first()
    if not unidade:
        raise HTTPException(status_code=404, detail="Unidade nao encontrada")

    novo = DesbravadorModel(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/desbravadores/", response_model=list[Desbravador])
def listar_desbravadores(db: Session = Depends(get_db)):
    return db.query(DesbravadorModel).all()
