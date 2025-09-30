import pg8000.dbapi as pg 
from database.config import DB_CONFIG

# Conectando com o banco
def get_connection():
    try:
        # A nova biblioteca usa os mesmos parâmetros, então o DB_CONFIG funciona!
        connection = pg.connect(**DB_CONFIG) # <-- MUDANÇA 2: Usa a função da nova biblioteca
        return connection
    except Exception as e:
        print("Erro ao conectar com o banco:", e)
        return None