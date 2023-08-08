from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"mensagem": "Olá fastAPI - TDS"}

@app.get("/profile")
async def profile():
    return {"name": "Gustavo Suguyama Orlanidni"}

@app.post("/profile")
async def signup():
    return {"mensagem": "Perfil criado com sucesso"}

@app.put("/profile")
async def atualizar():
    return {"mensagem": "Perfil atualizado com sucesso"}

@app.delete("/profile")
async def remover():
    return {"mensagem": "Perfil deletado com sucesso"}