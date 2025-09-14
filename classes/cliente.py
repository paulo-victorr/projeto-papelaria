# Classe cliente
class Cliente:
    def __init__(self, id=None, nome="", telefone="", email="", endereco=""):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    # Retorna dados básicos do cliente 
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}"