from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = -1
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}   
    else:  
        return {"error": "Nenhum animal encontrado"} 

@app.post('/animais')
def criar_animal(animal: Animal):
    if animal.id is None:
        animal.id = str(uuid4())
        banco.append(animal)
    return {"mensagem": f"{animal.nome} cadastrado com sucesso"}

