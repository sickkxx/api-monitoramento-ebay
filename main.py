from fastapi import FastAPI
from scrapper import ebay_scraper
from database import salvar_produtos, listar_produtos

app: FastAPI = FastAPI()

@app.get('/buscar/{produto}')
def buscar(produto: str):
    resultado = ebay_scraper(produto)

    for item in resultado:
        salvar_produtos(
            item["produto"],
            item["preco"],
            item["vendedor"],
            item["link"],
            item["data_coleta"]
        )

    return {"msg": "Dados salvos", "quantidade": len(resultado)}

@app.get("/produtos")
def produtos():
    return listar_produtos()