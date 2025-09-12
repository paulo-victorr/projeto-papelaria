import psycopg2
from database.config import DB_CONFIG

# Conectando com o banco
def get_connection():
    try:
        # cria a conexão
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        # caso dê erro
        print("Erro ao conectar com o banco:", e)
        return None