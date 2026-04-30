from fastapi import FastAPI
from scrapper import EbayScraper
from db.repository import ProdutoRepository

app = FastAPI()

@app.get('/buscar/{produto}')
def buscar(produto):
    repo = ProdutoRepository()
    bot_scrap = EbayScraper()

    try:
        bot_scrap.iniciar()
        bot_scrap.pesquisar_produtos(produto)

        produtos = bot_scrap.produtos()

        for item in produtos:
            repo.salvar(**item)

    finally:
        bot_scrap.fechar()

    return {"msg": "Dados salvos", "quantidade": len(produtos)}

@app.get("/produtos")
def listar_produtos():
    produtos = ProdutoRepository()
    df = produtos.listar()
    return df.to_dict(orient="records")
