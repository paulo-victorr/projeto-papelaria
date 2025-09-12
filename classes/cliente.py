# Classe cliente
class Cliente:
    def __init__(self, id=None, nome="", telefone="", email="", endereco=""):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    # Retorna os dados completos do cliente
    def get_dados(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"
    
    # Atualiza os dados de contato do cliente
    def atualizar_contato(self, novo_telefone, novo_email):
        self.telefone = novo_telefone
        self.email = novo_email
    
    # Retorna o endereco do cliente
    def obter_endereco(self):
        return self.endereco
    
    # Retorna dados básicos do cliente 
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}"