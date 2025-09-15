from gerenciador_CRUD.gerenciador import GerenciadorProdutos
from classes.produto import Produto

def testar_sistema():
    gerenciador = GerenciadorProdutos()
    
    caneta = Produto(None, "Caneta Azul", "Escritorio", 2.50, 100)
    if gerenciador.inserir(caneta):
        print("Produto inserido com sucesso!")
    
    print("\nLista de produtos:")
    produtos = gerenciador.listar_todos()
    for p in produtos:
        print(p)
    
    print("\nRelatorio:")
    relatorio = gerenciador.gerar_relatorio_produtos()
    print(relatorio)

if __name__ == "__main__":
    testar_sistema()