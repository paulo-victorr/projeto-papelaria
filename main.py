from gerenciador_CRUD.gerenciador import GerenciadorProdutos
from gerenciador_CRUD.gerenciador import GerenciadorClientes
from classes.produto import Produto
from classes.cliente import Cliente

# Funcao para mostrar menu de produtos
def menu_produtos():
    gerenciador_produto = GerenciadorProdutos()
    
    while True:
        print("\n--- GERENCIAR PRODUTOS ---")
        print("1. Cadastrar novo produto")
        print("2. Listar todos os produtos")
        print("3. Pesquisar produto por nome")
        print("4. Alterar produto")
        print("5. Remover produto")
        print("6. Gerar relatorio")
        print("7. Buscar por id")
        print("8. Voltar ao menu principal")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            # Cadastrar novo produto
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            preco = float(input("Preco: "))
            estoque = int(input("Quantidade em estoque: "))
            
            novo_produto = Produto(None, nome, categoria, preco, estoque)
            if gerenciador_produto.inserir(novo_produto):
                print("Produto cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar produto.")
                
        elif opcao == "2":
            # Listar todos os produtos
            produtos = gerenciador_produto.listar_todos()
            print("\n--- LISTA DE PRODUTOS ---")
            for produto in produtos:
                print(produto)
                
        elif opcao == "3":
            # Pesquisar por nome
            nome = input("Digite o nome para pesquisar: ")
            produtos = gerenciador_produto.pesquisar_por_nome(nome)
            print("\n--- RESULTADO DA PESQUISA ---")
            for produto in produtos:
                print(produto)
        
        elif opcao == "4":
            # Alterar produto
            id_produto = int(input("Digite o ID do produto que deseja alterar: "))

            print("Digite os novos dados do produto:")
            nome = input("Novo nome: ")
            categoria = input("Nova categoria: ")
            preco = float(input("Novo preço: "))
            quantidade = int(input("Nova quantidade em estoque: "))

            # Criação do objeto Produto usando named args
            novo_produto = Produto(
                nome=nome,
                categoria=categoria,
                preco=preco,
                quantidade_estoque=quantidade
            )

            sucesso = gerenciador_produto.alterar(id_produto, novo_produto)

            if sucesso:
                print("Produto alterado com sucesso!")
            else:
                print("Erro ao alterar produto ou ID não encontrado.")
        
        elif opcao == "5":
            # Remover produto
            id_produto = int(input("Digite o id do produto a ser removido: "))
            
            sucesso = gerenciador_produto.remover(id_produto)
            
            if sucesso:
                print("Produto removido com sucesso!")
            else:
                print("Nenhum produto encontrado com esse id, ou erro na remoção.")
                
        elif opcao == "6":
            # Gerar relatorio
            relatorio = gerenciador_produto.gerar_relatorio_produtos()
            print("\n--- RELATORIO ---")
            print(relatorio)
            
        elif opcao == "7":
            # Exibir um produto pelo id
            id_produto = int(input("Digite o id do produto a buscar: "))
            
            print(gerenciador_produto.exibir_um(id_produto))
                
        elif opcao == "8":
            # Voltar para menu
            break
            
        else:
            print("Opcao invalida!")

def menu_clientes():
    gerenciador_cliente = GerenciadorClientes()
    
    while True:
        print("\n--- GERENCIAR CLIENTES ---")
        print("1. Cadastrar novo cliente")
        print("2. Listar todos os clientes")
        print("3. Pesquisar cliente por nome completo")
        print("4. Alterar dados cliente")
        print("5. Remover cliente")
        print("6. Gerar relatorio")
        print("7. Buscar por id")
        print("8. Voltar ao menu principal")
        
        opcao = input("Escolha uma opcao: ")
    
        if opcao == "1":
            # Cadastrar novo produto
            nome = input("Nome do Cliente: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            endereco = input("Endereço: ")
            
            novo_cliente = Cliente(None, nome, telefone, email, endereco)
            if gerenciador_cliente.inserir(novo_cliente):
                print("Cliente cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar Cliente.")

        elif opcao == "2":
            # Listar todos os clientes
            clientes = gerenciador_cliente.listar_todos()
            print("\n--- LISTA DE CLIENTES ---")
            for cliente in clientes:
                print(cliente)
        
        elif opcao == "3":
            # Pesquisar por nome
            nome = input("Digite o nome para pesquisar: ")
            clientes = gerenciador_cliente.pesquisar_por_nome(nome)
            print("\n--- RESULTADO DA PESQUISA ---")
            for cliente in clientes:
                print(cliente)

        elif opcao == "4":
            # Alterar Cliente
            id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))

            print("Digite os novos dados do cliente:")
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            endereco = input("Novo endereco: ")

            # Criação do objeto Cliente usando named args
            novo_cliente = Cliente(
                nome=nome,
                telefone=telefone,
                email=email,
                endereco=endereco
            )

            sucesso = gerenciador_cliente.alterar(id_cliente, novo_cliente)

            if sucesso:
                print("Cliente alterado com sucesso!")
            else:
                print("Erro ao alterar Cliente ou ID não encontrado.")
        
        elif opcao == "5":
            # Remover Cliente
            id_cliente = int(input("Digite o id do Cliente a ser removido: "))
            
            sucesso = gerenciador_cliente.remover(id_cliente)
            
            if sucesso:
                print("Cliente removido com sucesso!")
            else:
                print("Nenhum Cliente encontrado com esse id, ou erro na remoção.")        
        
        elif opcao == "6":
            # Gerar relatorio
            relatorio = gerenciador_cliente.gerar_relatorio_clientes()
            print("\n--- RELATORIO ---")
            print(relatorio)            
        
        elif opcao == "7":
            # Exibir um produto pelo id
            id_cliente = int(input("Digite o id do cliente a buscar: "))
            
            print(gerenciador_cliente.exibir_um(id_cliente))
        
        elif opcao == "8":
            # Voltar para menu
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
        elif opcao == "2":
            menu_clientes()    
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida!")

# Executa o programa
if __name__ == "__main__":
    main()