class Venda:
    def __init__(self, id=None, data_venda=None, cliente_id=None, vendedor_id=None, 
                 forma_pagamento="", status_pagamento="PENDENTE", valor_total=0.0):
        self.id = id
        self.data_venda = data_venda
        self.cliente_id = cliente_id
        self.vendedor_id = vendedor_id
        self.forma_pagamento = forma_pagamento
        self.status_pagamento = status_pagamento
        self.valor_total = valor_total
    
    def __str__(self):
        return f"Venda ID: {self.id}, Total: R${self.valor_total:.2f}, Status: {self.status_pagamento}"