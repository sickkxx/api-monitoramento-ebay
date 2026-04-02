import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine

p = Path(__file__).resolve().parent
load_dotenv(p / '.env')

def get_database_url():
    return (
        f"mysql+pymysql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )

def conectar():
    return create_engine(get_database_url())