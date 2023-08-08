from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"mensagem": "Olá fastAPI - TDS assasaasassas"}

@app.get("/profile")
async def profile():
    return {"name": "Gustavo Suguyama Orlanidni"}