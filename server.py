from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"mensagem": "Olá fastAPI - TDS assasaasassas"}