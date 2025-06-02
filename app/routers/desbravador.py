from fastapi import APIRouter, HTTPException
from app.schemas.desbravador import DesbravadorCreate, DesbravadorComUnidade
from app.database import db
from bson import ObjectId

router = APIRouter()

@router.post("/desbravadores/", response_model=DesbravadorComUnidade)
async def criar_desbravador(dados: DesbravadorCreate):
    # Verifica se a unidade existe
    if not ObjectId.is_valid(dados.unidade_id):
        raise HTTPException(status_code=400, detail="ID da unidade inválido")

    unidade = await db.unidades.find_one({"_id": ObjectId(dados.unidade_id)})
    if not unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")

    novo = dados.model_dump()
    novo["unidade_id"] = ObjectId(novo["unidade_id"])  # salvar como ObjectId real
    res = await db.desbravadores.insert_one(novo)
    novo["_id"] = str(res.inserted_id)
    novo["unidade_id"] = str(novo["unidade_id"])
    return novo

@router.get("/desbravadores/", response_model=list[DesbravadorComUnidade])
async def listar_desbravadores():
    desbravadores = []
    cursor = db.desbravadores.find({})
    async for d in cursor:
        unidade = await db.unidades.find_one({"_id": d["unidade_id"]})
        if unidade:
            d["unidade"] = {
                "_id": str(unidade["_id"]),
                "nome": unidade["nome"],
                "diretor": unidade["diretor"]
            }
        else:
            d["unidade"] = None
        d["_id"] = str(d["_id"])
        del d["unidade_id"]  # remove o campo bruto
        desbravadores.append(d)
    return desbravadores