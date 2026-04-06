import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine

# define o caminho do diretório atual do arquivo
p = Path(__file__).resolve().parent
print(p)

# carrega as variáveis de ambiente do arquivo .env localizado nesse diretório
load_dotenv(p / '.env')


def get_database_url():
    # monta a URL de conexão com MySQL usando PyMySQL e variáveis de ambiente
    return (
        f"mysql+pymysql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )


def conectar():
    # cria e retorna a engine SQLAlchemy para conectar ao banco
    return create_engine(get_database_url())