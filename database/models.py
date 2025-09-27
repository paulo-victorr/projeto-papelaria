from database.connection import get_connection

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
                quantidade_estoque INTEGER NOT NULL,
                fabricado_mari BOOLEAN DEFAULT false
            )
        """)
        
        # tabela de clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                telefone VARCHAR(20),
                email VARCHAR(100),
                endereco TEXT,
                cidade VARCHAR(50),
                time_futebol VARCHAR(30),
                assiste_one_piece BOOLEAN DEFAULT false
            )
        """)
        
        # tabela de vendedores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendedores (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                ativo BOOLEAN DEFAULT true
            )
        """)
        
        # tabela de vendas - constraints
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id SERIAL PRIMARY KEY,
                data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                cliente_id INTEGER REFERENCES cliente(id),
                vendedor_id INTEGER REFERENCES vendedores(id),
                forma_pagamento VARCHAR(20) CHECK (forma_pagamento IN ('CARTAO', 'BOLETO', 'PIX', 'BERRIES')),
                status_pagamento VARCHAR(20) DEFAULT 'PENDENTE' CHECK (status_pagamento IN ('PENDENTE', 'CONFIRMADO')),
                valor_total DECIMAL(10,2)
            )
        """)
        
        # tabela de itens_venda - constraint
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_venda (
                id SERIAL PRIMARY KEY,
                venda_id INTEGER REFERENCES vendas(id),
                produto_id INTEGER REFERENCES produto(id),
                quantidade INTEGER NOT NULL CHECK (quantidade > 0),
                preco_unitario DECIMAL(10,2) NOT NULL
            )
        """)
        
        # criar indices para melhorar performance
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_vendas_data ON vendas(data_venda)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_vendas_cliente ON vendas(cliente_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_produto_categoria ON produto(categoria)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_produto_preco ON produto(preco)")
        
        conn.commit()
        print("Tabelas criadas com sucesso")
        return True
        
    except Exception as e:
        print("Erro ao criar tabelas:", e)
        return False
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_tables()