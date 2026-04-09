from fastapi import FastAPI
from scrapper import EbayScraper
from db.repository import ProdutoRepository

app: FastAPI = FastAPI()

@app.get('/buscar/{produto}')
def buscar(produto: str) -> dict[str, str | int]:
    repo = ProdutoRepository()
    scrap = EbayScraper()

    try:
        resultado = scrap.buscar(produto)

        for item in resultado:
            repo.salvar(**item)

    finally:
        scrap.fechar()

    return {"msg": "Dados salvos", "quantidade": len(resultado)}

@app.get("/produtos")
def produtos():
    listar_produtos = ProdutoRepository()
    df = listar_produtos.listar()
    return df.to_dict(orient="records")
