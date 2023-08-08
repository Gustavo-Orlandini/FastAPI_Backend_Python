from uuid import uuid4
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()
class Animal(BaseModel):
    id: int = None
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get("/animais")
async def listar_animais():
    return banco

@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {"error": "Nenhum animal encontrado"}    

@app.post('/animais')
def criar_animal(animal: Animal):
    if animal.id is None:
        animal.id = str(uuid4())
        banco.append(animal)
    return {"mensagem": f"{animal.nome} cadastrado com sucesso"}

