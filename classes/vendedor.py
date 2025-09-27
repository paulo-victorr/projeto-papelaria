class Vendedor:
    def __init__(self, id=None, nome="", email="", ativo=True):
        self.id = id
        self.nome = nome
        self.email = email
        self.ativo = ativo
    
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}"