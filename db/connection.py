import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine

p = Path(__file__).resolve().parent.parent
load_dotenv(p / '.env')

class Conexao:
    def __init__(self):
        self.url_database = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        self.engine = create_engine(self.url_database)

    def conectar(self):
        return self.engine
