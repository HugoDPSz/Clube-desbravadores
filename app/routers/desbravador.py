from fastapi import APIRouter, HTTPException
from app.schemas.desbravador import DesbravadorCreate, Desbravador
from app.database import db
from bson import ObjectId

router = APIRouter()

@router.post("/desbravadores/", response_model=Desbravador)
async def criar_desbravador(dados: DesbravadorCreate):
    novo = dados.model_dump()
    res = await db.desbravadores.insert_one(novo)
    novo["_id"] = str(res.inserted_id)
    return novo

@router.get("/desbravadores/", response_model=list[Desbravador])
async def listar_desbravadores():
    desbravadores = []
    cursor = db.desbravadores.find({})
    async for d in cursor:
        d["_id"] = str(d["_id"])
        desbravadores.append(d)
    return desbravadores