# investigar_banco.py
from database.connection import get_connection

def investigar():
    print("🔍 INVESTIGAÇÃO COMPLETA DO BANCO")
    print("=" * 50)
    
    conn = get_connection()
    if conn is None:
        return
    
    try:
        with conn.cursor() as cursor:
            # 1. Verificar em qual banco estamos
            cursor.execute("SELECT current_database(), current_user")
            banco, usuario = cursor.fetchone()
            print(f"📊 Banco: {banco}")
            print(f"👤 Usuário: {usuario}")
            print("-" * 30)
            
            # 2. Listar TODOS os bancos disponíveis
            cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false")
            bancos = cursor.fetchall()
            print("🗄️ Bancos disponíveis:")
            for banco in bancos:
                print(f"   ➤ {banco[0]}")
            print("-" * 30)
            
            # 3. Verificar SE as tabelas existem neste banco
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tabelas = cursor.fetchall()
            
            print("📋 Tabelas no banco atual:")
            if tabelas:
                for tabela in tabelas:
                    print(f"   ✅ {tabela[0]}")
            else:
                print("   ❌ NENHUMA TABELA ENCONTRADA!")
            print("-" * 30)
            
            # 4. Tentar criar as tabelas AGORA
            print("🛠️ Tentando criar tabelas AGORA...")
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS produto (
                        id SERIAL PRIMARY KEY,
                        nome VARCHAR(100) NOT NULL,
                        categoria VARCHAR(50),
                        preco DECIMAL(10,2) NOT NULL,
                        quantidade_estoque INTEGER NOT NULL
                    )
                """)
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
                print("✅ Tabelas criadas COM SUCESSO!")
            except Exception as e:
                print(f"❌ Erro ao criar tabelas: {e}")
                conn.rollback()
                
    except Exception as e:
        print(f"❌ Erro na investigação: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    investigar()