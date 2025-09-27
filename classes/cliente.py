# Classe cliente atualizada
class Cliente:
    def __init__(self, id=None, nome="", telefone="", email="", endereco="", 
                 cidade="", time_futebol="", assiste_one_piece=False):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.cidade = cidade
        self.time_futebol = time_futebol
        self.assiste_one_piece = assiste_one_piece
    
    def tem_desconto_flamengo(self):
        return self.time_futebol == "Flamengo"
    
    def tem_desconto_one_piece(self):
        return self.assiste_one_piece
    
    def tem_desconto_sousa(self):
        return self.cidade == "Sousa"
    
    def calcular_desconto(self):
        desconto = 0
        if self.tem_desconto_flamengo():
            desconto += 5
        if self.tem_desconto_one_piece():
            desconto += 5
        if self.tem_desconto_sousa():
            desconto += 5
        return desconto
    
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Cidade: {self.cidade}"