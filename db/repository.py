import pandas as pd
from sqlalchemy import text
from .connection import Conexao

class ProdutoRepository:
    def __init__(self):
        self.engine = Conexao().conectar()
        self.query = text(
            """
            INSERT INTO produtos (produto, preco, vendedor, link, data_coleta) 
            VALUES (:produto, :preco, :vendedor, :link, :data_coleta) 
                ON DUPLICATE KEY UPDATE preco = VALUES(preco), link = VALUES(link), data_coleta = VALUES(data_coleta)
            """
        )

    def salvar(self, **dados):
        with self.engine.begin() as conn: # type: ignore
            conn.execute(self.query, dados)

    def listar(self):
        return pd.read_sql("SELECT * FROM produtos", self.engine)
