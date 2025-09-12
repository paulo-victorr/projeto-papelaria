# gerenciador_CRUD/gerenciador.py
from database.connection import get_connection
from classes.produto import Produto

# Classe para gerenciar os CRUD
class GerenciadorProdutos:
    
    # Insere um novo produto no banco
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
    
    # Retorna todos os produtos do banco
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
            
     # Pesquisa produtos por nome
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
    
    # Busca um produto pelo ID
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
    
    # Atualiza um produto existente
    def alterar(self, id, produto):
        conn = get_connection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE produto SET nome = %s, categoria = %s, preco = %s, quantidade_estoque = %s WHERE id = %s",
                (produto.nome, produto.categoria, produto.preco, produto.quantidade_estoque, id)
            )
            conn.commit()
            # Verifica se alguma linha foi alterada
            return cursor.rowcount > 0
        except Exception as e:
            print("Erro ao alterar produto:", e)
            return False
        finally:
            conn.close()
    
    # Remove um produto pelo ID
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
    
    # Gera relatorio de produtos
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