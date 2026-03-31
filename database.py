import mysql.connector

def conectar() -> "mysql.connector.connection.MySQLConnection":
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",
        database="ebay_produtos"
    )

def salvar_produtos(produto: str, preco: float, vendedor: str, link: str, data_coleta: object) -> None:
    conn: "mysql.connector.connection.MySQLConnection" = conectar()
    cursor: "mysql.connector.cursor.MySQLCursor" = conn.cursor()

    query: str = """INSERT INTO produtos (produto, preco, vendedor, link, data_coleta) VALUES (%s, %s, %s, %s, %s)"""

    cursor.execute(query, (produto, preco, vendedor, link, data_coleta))
    conn.commit()

    cursor.close()
    conn.close()

def listar_produtos() -> list[dict]:
    conn: "mysql.connector.connection.MySQLConnection" = conectar()
    cursor: "mysql.connector.cursor.MySQLCursorDict" = conn.cursor(dictionary=True)

    cursor.execute("""SELECT * FROM produtos""")

    resultados: list[dict] = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultados
