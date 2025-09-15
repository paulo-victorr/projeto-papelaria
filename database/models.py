from database.connection import get_connection

# Funcao create_tables para criar as tabelas que vamos utilizar
def create_tables():
    conn = get_connection()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        
        # tabela de produtos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco DECIMAL(10,2) NOT NULL,
                quantidade_estoque INTEGER NOT NULL
            )
        """)
        
        # tabela de clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                telefone VARCHAR(20),
                email VARCHAR(100),
                endereco TEXT
            )
        """)
        
        conn.commit()
        print("Tabelas criadas")
        return True
        
    except Exception as e:
        print("Erro ao criar tabelas:", e)
        return False
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_tables()