from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/saudacao/{nome}")
async def home(nome: str):
    texto = f'Olá {nome}, seja bem vindo!'
    return {"mensagem": texto}

@app.get("/quadrado/{numero}")
async def home(numero: int):
    resultado = numero * numero
    texto = f'O quadrado de {numero}, é {resultado}!'
    return {"mensagem": texto}

class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produtos')
def produtos(produto: Produto):
    return {"mensagem": f'Produto ({produto}) cadastrado com sucesso!'}