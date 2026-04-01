import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",
        database="ebay_produtos"
    )

def salvar_produtos(produto, preco, vendedor, link, data_coleta):
    conn = conectar()
    cursor = conn.cursor()

    query = """INSERT IGNORE INTO produtos (produto, preco, vendedor, link, data_coleta) VALUES (%s, %s, %s, %s, %s)"""

    cursor.execute(query, (produto, preco, vendedor, link, data_coleta))
    conn.commit()

    cursor.close()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""SELECT * FROM produtos""")

    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultados
