from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://hugo:MiluBr2004@clubedesbravadores.9lxo3kf.mongodb.net/?retryWrites=true&w=majority&appName=clubedesbravadores"
client = AsyncIOMotorClient(MONGO_URL)
db = client["clube_desbravadores"]