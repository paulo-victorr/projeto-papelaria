from database.connection import get_connection

def testar_conexao():
    conn = get_connection()
    
    if conn:
        print("Conexao com o banco realizada com sucesso!")
        conn.close()
    else:
        print("Erro: Nao foi possivel conectar ao banco de dados")

if __name__ == "__main__":
    testar_conexao()