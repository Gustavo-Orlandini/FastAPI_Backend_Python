from fastapi import FastAPI

app = FastAPI()

@app.get("/saudacao/{nome}")
async def home(nome):
    return nome

