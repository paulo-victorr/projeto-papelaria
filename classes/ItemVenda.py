# Classe item_venda
class ItemVenda:
    def __init__(self, id=None, venda_id=None, produto_id=None, quantidade=0, preco_unitario=0.0):
        self.id = id
        self.venda_id = venda_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
    
    def calcular_subtotal(self):
        return self.quantidade * self.preco_unitario
    
    def __str__(self):
        return f"Item: {self.quantidade} unidades - Subtotal: R${self.calcular_subtotal():.2f}"