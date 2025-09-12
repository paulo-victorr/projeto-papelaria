from gerenciador_CRUD.gerenciador import GerenciadorProdutos
from classes.produto import Produto

# Funcao para mostrar menu de produtos
def menu_produtos():
    gerenciador = GerenciadorProdutos()
    
    while True:
        print("\n--- GERENCIAR PRODUTOS ---")
        print("1. Cadastrar novo produto")
        print("2. Listar todos os produtos")
        print("3. Pesquisar produto por nome")
        print("4. Alterar produto")
        print("5. Remover produto")
        print("6. Gerar relatorio")
        print("7. Voltar ao menu principal")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            # Cadastrar novo produto
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            preco = float(input("Preco: "))
            estoque = int(input("Quantidade em estoque: "))
            
            novo_produto = Produto(None, nome, categoria, preco, estoque)
            if gerenciador.inserir(novo_produto):
                print("Produto cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar produto.")
                
        elif opcao == "2":
            # Listar todos os produtos
            produtos = gerenciador.listar_todos()
            print("\n--- LISTA DE PRODUTOS ---")
            for produto in produtos:
                print(produto)
                
        elif opcao == "3":
            # Pesquisar por nome
            nome = input("Digite o nome para pesquisar: ")
            produtos = gerenciador.pesquisar_por_nome(nome)
            print("\n--- RESULTADO DA PESQUISA ---")
            for produto in produtos:
                print(produto)
                
        elif opcao == "6":
            # Gerar relatorio
            relatorio = gerenciador.gerar_relatorio_produtos()
            print("\n--- RELATORIO ---")
            print(relatorio)
            
        elif opcao == "7":
            break
            
        else:
            print("Opcao invalida!")

# Funcao principal
def main():
    while True:
        print("\n=== SISTEMA PAPELARIA ===")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Clientes")
        print("3. Sair")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            menu_produtos()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida!")

# Executa o programa
if __name__ == "__main__":
    main()