class Produto:
    def __init__(self, id=None, nome="", categoria="", preco=0.0, quantidade_estoque=0):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        
    # Retorna os dados do produto 
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}, Estoque: {self.quantidade_estoque}"