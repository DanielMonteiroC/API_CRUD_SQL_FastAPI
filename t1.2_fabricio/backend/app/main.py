from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ← Importado para CORS
from . import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# ← Adicionado middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique seu domínio ex: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.get("/")
def raiz():
    return {"mensagem": "API FastAPI com MySQL funcionando!"}
