from fastapi import APIRouter
from app.schemas.unidade import UnidadeCreate, Unidade
from app.database import db

router = APIRouter()

@router.post("/unidades/", response_model=Unidade)
async def criar_unidade(dados:UnidadeCreate):
    nova = dados.model_dump()
    res = await db.unidades.insert_one(nova)
    nova["_id"] = str(res.inserted_id)
    return nova

@router.get("/unidades/", response_model=list[Unidade])
async def listar_unidades():
    unidades = []
    cursor = db.unidades.find({})
    async for u in cursor:
        u["_id"] = str(u["_id"])
        unidades.append(u)
    return unidades