import psycopg2
from database.config import DB_CONFIG

# Conectando com o banco
def get_connection():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print("Erro ao conectar com o banco:", e)
        return None