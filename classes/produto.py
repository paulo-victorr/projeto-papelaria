from decimal import Decimal

# Classe produto atualizada
class Produto:
    def __init__(self, id=None, nome="", categoria="", preco=0.0, quantidade_estoque=0, fabricado_mari=False):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = Decimal(str(preco))
        self.quantidade_estoque = quantidade_estoque
        self.fabricado_mari = fabricado_mari
    
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}, Estoque: {self.quantidade_estoque}"