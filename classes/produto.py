# Classe do produto
class Produto:
    def __init__(self, id=None, nome="", categoria="", preco=0.0, quantidade_estoque=0):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
    
    # Atualiza a quantidade em estoque
    def atualizar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        return self.quantidade_estoque
    
    # Verifica se o produto esta disponivel
    def verificar_disponibilidade(self):
        return self.quantidade_estoque > 0
    
    # Aplica desconto no preco do produto
    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco = self.preco - desconto
        return self.preco
    
    # Retorna os dados do produto 
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}, Estoque: {self.quantidade_estoque}"