from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()
class Animal(BaseModel):
    id: int
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get("animais")
async def listar_animais():
    return banco

@app.post('/animais')
def criar_animal(animal: Animal):
    banco.append(animal)
    return {"mensagem": f"{animal.nome} cadastrado com sucesso"}

