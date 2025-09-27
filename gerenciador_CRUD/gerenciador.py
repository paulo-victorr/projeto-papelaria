from database.connection import get_connection
from classes.produto import Produto
from classes.cliente import Cliente
from classes.vendedor import Vendedor
from classes.venda import Venda
from classes.item_venda import ItemVenda

class GerenciadorProdutos:
    
    def inserir(self, produto):
        conn = get_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO produto (nome, categoria, preco, quantidade_estoque) VALUES (%s, %s, %s, %s) RETURNING id",
                (produto.nome, produto.categoria, produto.preco, produto.quantidade_estoque)
            )
            # Pega o ID gerado automaticamente
            produto.id = cursor.fetchone()[0]
            conn.commit()
            return True
        except Exception as e:
            print("Erro ao inserir produto:", e)
            return False
        finally:
            conn.close()
    
    def listar_todos(self):
        conn = get_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produto ORDER BY nome")
            resultados = cursor.fetchall()
            
            produtos = []
            for linha in resultados:
                # Cria objeto Produto para cada linha do banco
                produto = Produto(linha[0], linha[1], linha[2], float(linha[3]), linha[4])
                produtos.append(produto)
            
            return produtos
        except Exception as e:
            print("Erro ao listar produtos:", e)
            return []
        finally:
            conn.close()
                
    def pesquisar_por_nome(self, nome):
        conn = get_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            # Busca produtos que contenham o nome pesquisado
            cursor.execute("SELECT * FROM produto WHERE nome ILIKE %s ORDER BY nome", (f'%{nome}%',))
            resultados = cursor.fetchall()
            
            produtos = []
            for linha in resultados:
                produto = Produto(linha[0], linha[1], linha[2], float(linha[3]), linha[4])
                produtos.append(produto)
            
            return produtos
        except Exception as e:
            print("Erro ao pesquisar produtos:", e)
            return []
        finally:
            conn.close()
    
    def exibir_um(self, id):
        conn = get_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produto WHERE id = %s", (id,))
            linha = cursor.fetchone()
            
            if linha:
                return Produto(linha[0], linha[1], linha[2], float(linha[3]), linha[4])
            return None
        except Exception as e:
            print("Erro ao buscar produto:", e)
            return None
        finally:
            conn.close()
    
    def alterar(self, id, produto):
        conn = get_connection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE produto
                SET nome = %s, categoria = %s, preco = %s, quantidade_estoque = %s
                WHERE id = %s
            """

            # suporte para vários formatos de 'produto'
            if isinstance(produto, (tuple, list)) and len(produto) >= 4:
                nome, categoria, preco, quantidade_estoque = produto[:4]
            elif isinstance(produto, dict):
                nome = produto.get("nome")
                categoria = produto.get("categoria")
                preco = produto.get("preco")
                quantidade_estoque = produto.get("quantidade_estoque")
            else:
                nome = produto.nome
                categoria = produto.categoria
                preco = produto.preco
                quantidade_estoque = produto.quantidade_estoque

            valores = (
                str(nome),
                str(categoria),
                float(preco),
                int(quantidade_estoque),
                int(id)
            )

            cursor.execute(sql, valores)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Erro ao alterar produto:", e)
            return False
        finally:
            conn.close()
    
    def remover(self, id):
        conn = get_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produto WHERE id = %s", (id,))
            conn.commit()
            # Verifica se alguma linha foi removida
            return cursor.rowcount > 0
        except Exception as e:
            print("Erro ao remover produto:", e)
            return False
        finally:
            conn.close()
    
    def gerar_relatorio_produtos(self):
        conn = get_connection()
        if conn is None:
            return "Erro de conexao"
        
        try:
            cursor = conn.cursor()
            
            # Total de produtos
            cursor.execute("SELECT COUNT(*) FROM produto")
            total = cursor.fetchone()[0]
            
            # Valor total do estoque
            cursor.execute("SELECT SUM(preco * quantidade_estoque) FROM produto")
            valor_total = cursor.fetchone()[0] or 0
            
            # Produtos com estoque baixo
            cursor.execute("SELECT COUNT(*) FROM produto WHERE quantidade_estoque < 10")
            estoque_baixo = cursor.fetchone()[0]
            
            return (f"RELATORIO DE PRODUTOS\n"
                    f"Total de produtos: {total}\n"
                    f"Valor total em estoque: R$ {valor_total:.2f}\n"
                    f"Produtos com estoque baixo: {estoque_baixo}")
                    
        except Exception as e:
            return f"Erro ao gerar relatorio: {e}"
        finally:
            conn.close()
            
class GerenciadorClientes:
    
    def inserir(self, cliente):
        conn = get_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cliente (nome, telefone, email, endereco) VALUES (%s, %s, %s, %s) RETURNING id",
                (cliente.nome, cliente.telefone, cliente.email, cliente.endereco)
            )
            # Pega o ID gerado automaticamente
            cliente.id = cursor.fetchone()[0]
            conn.commit()
            return True
        except Exception as e:
            print("Erro ao inserir Cliente:", e)
            return False
        finally:
            conn.close()      
            
    def listar_todos(self):
        conn = get_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cliente ORDER BY nome")
            resultados = cursor.fetchall()
            
            clientes = []
            for linha in resultados:
                # Cria objeto clientes para cada linha do banco
                cliente = Cliente(linha[0], linha[1], linha[2], (linha[3]), linha[4])
                clientes.append(cliente)
            
            return clientes
        except Exception as e:
            print("Erro ao listar Clientes:", e)
            return []
        finally:
            conn.close()
    
    def pesquisar_por_nome(self, nome):
        conn = get_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cliente WHERE nome ILIKE %s ORDER BY nome", (f'%{nome}%',))
            resultados = cursor.fetchall()
            
            clientes = []
            for linha in resultados:
                cliente = Cliente(linha[0], linha[1], linha[2], (linha[3]), linha[4])
                clientes.append(cliente)
            
            return clientes
        except Exception as e:
            print("Erro ao pesquisar clientes:", e)
            return []
        finally:
            conn.close() 
    
    def alterar(self, id, cliente):
        conn = get_connection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE cliente
                SET nome = %s, telefone = %s, email = %s, endereco = %s
                WHERE id = %s
            """

            # suporte para vários formatos de 'produto'
            if isinstance(cliente, (tuple, list)) and len(cliente) >= 4:
                nome, telefone, email, endereco = cliente[:4]
            elif isinstance(cliente, dict):
                nome = cliente.get("nome")
                telefone = cliente.get("telefone")
                email = cliente.get("email")
                endereco = cliente.get("endereco")
            else:
                nome = cliente.nome
                telefone = cliente.telefone
                email = cliente.email
                endereco = cliente.endereco

            valores = (
                str(nome),
                str(telefone),
                str(email),
                str(endereco),
                int(id)
            )

            cursor.execute(sql, valores)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Erro ao alterar cliente:", e)
            return False
        finally:
            conn.close()

    def remover(self, id):
        conn = get_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))
            conn.commit()
            # Verifica se alguma linha foi removida
            return cursor.rowcount > 0
        except Exception as e:
            print("Erro ao remover cliente:", e)
            return False
        finally:
            conn.close()

    def gerar_relatorio_clientes(self):
        conn = get_connection()
        if conn is None:
            return "Erro de conexao"
        
        try:
            cursor = conn.cursor()
            
            # Total de clientes
            cursor.execute("SELECT COUNT(*) FROM cliente")
            total = cursor.fetchone()[0]
            
            # Clientes sem telefone
            cursor.execute("SELECT COUNT(*) FROM cliente WHERE telefone IS NULL OR telefone = ''")
            sem_telefone = cursor.fetchone()[0]
            
            # Clientes sem email
            cursor.execute("SELECT COUNT(*) FROM cliente WHERE email IS NULL OR email = ''")
            sem_email = cursor.fetchone()[0]
            
            # Endereços mais comuns
            cursor.execute("SELECT endereco, COUNT(*) FROM cliente GROUP BY endereco ORDER BY COUNT(*) DESC LIMIT 3")
            top_enderecos = cursor.fetchall()
            
            relatorio = (f"RELATÓRIO DE CLIENTES\n"
                        f"Total de clientes: {total}\n"
                        f"Sem telefone: {sem_telefone}\n"
                        f"Sem email: {sem_email}\n"
                        f"\nTop 3 endereços mais cadastrados:\n")
            
            for endereco, qtd in top_enderecos:
                relatorio += f" - {endereco}: {qtd} clientes\n"
            
            return relatorio
            
        except Exception as e:
            return f"Erro ao gerar relatório: {e}"
        finally:
            conn.close()
    
    def exibir_um(self, id):
        conn = get_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,))
            linha = cursor.fetchone()
            
            if linha:
                return Cliente(linha[0], linha[1], linha[2], (linha[3]), linha[4])
            return None
        except Exception as e:
            print("Erro ao buscar cliente:", e)
            return None
        finally:
            conn.close()

class GerenciadorVendedores:

    #Cadastramento de vendedores
    def inserir(self, vendedor):
        conn = get_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO vendedores (nome, email) VALUES (%s, %s) RETURNING id",
                (vendedor.nome, vendedor.email)
            )
            vendedor.id = cursor.fetchone()[0]
            conn.commit()
            return True
        except Exception as e:
            print("Erro ao inserir vendedor:", e)
            return False
        finally:
            conn.close()
    
    # Listar todos os vendedores cadastrados
    def listar_todos(self):
        conn = get_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendedores ORDER BY nome")
            resultados = cursor.fetchall()
            
            vendedores = []
            for linha in resultados:
                vendedor = Vendedor(linha[0], linha[1], linha[2])
                vendedores.append(vendedor)
            
            return vendedores
        except Exception as e:
            print("Erro ao listar vendedores:", e)
            return []
        finally:
            conn.close()

class GerenciadorVendas:
    
    def realizar_venda(self, venda, itens):
        conn = get_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            
            # Verificar estoque antes de vender
            for item in itens:
                cursor.execute("SELECT quantidade_estoque FROM produto WHERE id = %s", (item.produto_id,))
                quantidade_estoque = cursor.fetchone()[0]
                if quantidade_estoque < item.quantidade:
                    print("Erro: Estoque insuficiente")
                    return False
            
            # Verificar forma de pagamento
            formas_confirmadas = ['CARTAO', 'BOLETO', 'PIX', 'BERRIES']
            if venda.forma_pagamento in formas_confirmadas:
                venda.status_pagamento = 'CONFIRMADO'
            else:
                venda.status_pagamento = 'PENDENTE'
            
            # Inserir venda
            cursor.execute(
                """INSERT INTO vendas (cliente_id, vendedor_id, forma_pagamento, status_pagamento, valor_total) 
                   VALUES (%s, %s, %s, %s, %s) RETURNING id""",
                (venda.cliente_id, venda.vendedor_id, venda.forma_pagamento, venda.status_pagamento, venda.valor_total)
            )
            venda_id = cursor.fetchone()[0]
            
            # Inserir itens e atualizar estoque
            for item in itens:
                cursor.execute(
                    "INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
                    (venda_id, item.produto_id, item.quantidade, item.preco_unitario)
                )
                # Atualizar estoque
                cursor.execute(
                    "UPDATE produto SET quantidade_estoque = quantidade_estoque - %s WHERE id = %s",
                    (item.quantidade, item.produto_id)
                )
            
            conn.commit()
            print("Venda realizada com sucesso!")
            return True
        except Exception as e:
            print("Erro ao realizar venda:", e)
            conn.rollback()
            return False
        finally:
            conn.close()
    
    # Listar pedidos do cliente
    def listar_vendas_por_cliente(self, cliente_id):
        conn = get_connection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM vendas WHERE cliente_id = %s ORDER BY data_venda DESC",
                (cliente_id,)
            )
            resultados = cursor.fetchall()
            
            vendas = []
            for linha in resultados:
                venda = Venda(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], float(linha[6]))
                vendas.append(venda)
            
            return vendas
        except Exception as e:
            print("Erro ao listar vendas do cliente:", e)
            return []
        finally:
            conn.close()

class GerenciadorRelatorios:
    def relatorio_vendas_vendedor(self, mes, ano):
        conn = get_connection()
        if conn is None:
            return "Erro de conexão"
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT v.nome as vendedor, COUNT(vd.id) as total_vendas, SUM(vd.valor_total) as valor_total
                FROM vendas vd
                JOIN vendedores v ON vd.vendedor_id = v.id
                WHERE EXTRACT(MONTH FROM vd.data_venda) = %s AND EXTRACT(YEAR FROM vd.data_venda) = %s
                GROUP BY v.id, v.nome
                ORDER BY valor_total DESC
            """, (mes, ano))
            
            resultados = cursor.fetchall() 
            relatorio = f"RELATÓRIO DE VENDAS - {mes}/{ano}\n"
            relatorio += "=" * 50 + "\n"
            
            for linha in resultados:
                relatorio += f"Vendedor: {linha[0]}\n"
                relatorio += f"Total de vendas: {linha[1]}\n"
                relatorio += f"Valor total: R$ {linha[2]:.2f}\n"
                relatorio += "-" * 30 + "\n"
            
            return relatorio
        except Exception as e:
            return f"Erro ao gerar relatório: {e}"
        finally:
            conn.close()