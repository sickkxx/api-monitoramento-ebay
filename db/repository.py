import pandas as pd
from sqlalchemy import text
from connection import conectar


def salvar_produtos(produto, preco, vendedor, link, data_coleta) -> None:
    engine = conectar()

    query = text(
        """
        INSERT INTO produtos (produto, preco, vendedor, link, data_coleta) 
        VALUES (:produto, :preco, :vendedor, :link, :data_coleta) 
            ON DUPLICATE KEY UPDATE preco = VALUES(preco), link = VALUES(link), data_coleta = VALUES(data_coleta)
        """
    )

    with engine.begin() as conn: # type: ignore
        conn.execute(query, {
            "produto": produto,
            "preco": preco,
            "vendedor": vendedor,
            "link": link,
            "data_coleta": data_coleta
        })

def listar_produtos() -> pd.DataFrame:
    engine = conectar()

    df: pd.DataFrame = pd.read_sql(
        "SELECT * FROM produtos",
        engine
    )

    return df
