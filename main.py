from fastapi import FastAPI
from scrapper import ebay_scraper
from projetos.ebay_scrapper.db.repository import salvar_produtos, listar_produtos

app: FastAPI = FastAPI()

@app.get('/buscar/{produto}')
def buscar(produto: str) -> dict[str, str | int]:
    resultado: list[dict[str, str | float | object]] = ebay_scraper(produto)

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
    df = listar_produtos()
    return df.to_dict(orient="records")
