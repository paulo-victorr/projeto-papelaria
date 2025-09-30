from gerenciador_CRUD.gerenciador import GerenciadorProdutos
from gerenciador_CRUD.gerenciador import GerenciadorClientes, GerenciadorRelatorios
from classes.produto import Produto
from classes.cliente import Cliente
import time
import os  

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# No seu arquivo main.py

def menu_produtos():
    gerenciador_produto = GerenciadorProdutos()
    
    while True:
        print("\n--- GERENCIAR PRODUTOS ---")
        print("1. Cadastrar novo produto")
        print("2. Listar todos os produtos")
        print("3. Pesquisar produtos (menu de filtros)") # ALTERADO
        print("4. Alterar produto")
        print("5. Remover produto")
        print("6. Gerar relatorio")
        print("7. Buscar por id")
        print("8. Voltar ao menu principal")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            preco = float(input("Preco: "))
            estoque = int(input("Quantidade em estoque: "))
            # NOVO: Perguntar se o produto é fabricado em Mari
            fabricado_mari_str = input("É fabricado em Mari? (s/n): ")
            fabricado_mari = True if fabricado_mari_str.lower() == 's' else False
            
            novo_produto = Produto(None, nome, categoria, preco, estoque, fabricado_mari)
            if gerenciador_produto.inserir(novo_produto):
                print("Produto cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar produto.")
            time.sleep(2)
                
        elif opcao == "2":
            produtos = gerenciador_produto.listar_todos()
            print("\n--- LISTA DE PRODUTOS ---")
            for produto in produtos:
                print(produto)
            time.sleep(10)
                
        # NOVO: Submenu de pesquisa
        elif opcao == "3":
            while True:
                print("\n--- MENU DE PESQUISA DE PRODUTOS ---")
                print("1. Pesquisar por nome")
                print("2. Pesquisar por categoria")
                print("3. Pesquisar por faixa de preço")
                print("4. Listar fabricados em Mari")
                print("5. Voltar")
                
                sub_opcao = input("Escolha o tipo de pesquisa: ")
                
                produtos_encontrados = []
                if sub_opcao == "1":
                    nome = input("Digite o nome para pesquisar: ")
                    produtos_encontrados = gerenciador_produto.pesquisar_por_nome(nome)
                elif sub_opcao == "2":
                    categoria = input("Digite a categoria para pesquisar: ")
                    produtos_encontrados = gerenciador_produto.pesquisar_por_categoria(categoria)
                elif sub_opcao == "3":
                    try:
                        preco_min = float(input("Digite o preço mínimo: "))
                        preco_max = float(input("Digite o preço máximo: "))
                        produtos_encontrados = gerenciador_produto.pesquisar_por_faixa_de_preco(preco_min, preco_max)
                    except ValueError:
                        print("Erro: Preços inválidos. Por favor, digite números.")
                elif sub_opcao == "4":
                    produtos_encontrados = gerenciador_produto.pesquisar_fabricados_em_mari()
                elif sub_opcao == "5":
                    break
                else:
                    print("Opção inválida!")

                print("\n--- RESULTADO DA PESQUISA ---")
                if produtos_encontrados:
                    for produto in produtos_encontrados:
                        print(produto)
                else:
                    print("Nenhum produto encontrado com os critérios informados.")
                time.sleep(7)
        
        elif opcao == "4":
            id_produto = int(input("Digite o ID do produto que deseja alterar: "))
            produto_existente = gerenciador_produto.exibir_um(id_produto)
            if not produto_existente:
                print("Produto não encontrado.")
                time.sleep(2)
                continue
            
            print("Digite os novos dados (deixe em branco para manter o valor atual):")
            nome = input(f"Novo nome ({produto_existente.nome}): ") or produto_existente.nome
            categoria = input(f"Nova categoria ({produto_existente.categoria}): ") or produto_existente.categoria
            preco_str = input(f"Novo preço ({produto_existente.preco}): ")
            preco = float(preco_str) if preco_str else produto_existente.preco
            estoque_str = input(f"Nova quantidade ({produto_existente.quantidade_estoque}): ")
            estoque = int(estoque_str) if estoque_str else produto_existente.quantidade_estoque
            fabricado_mari_str = input(f"Fabricado em Mari? (s/n) ({'s' if produto_existente.fabricado_mari else 'n'}): ")
            fabricado_mari = (True if fabricado_mari_str.lower() == 's' else False) if fabricado_mari_str else produto_existente.fabricado_mari

            produto_atualizado = Produto(id_produto, nome, categoria, preco, estoque, fabricado_mari)
            if gerenciador_produto.alterar(id_produto, produto_atualizado):
                print("Produto alterado com sucesso!")
            else:
                print("Erro ao alterar produto.")
            time.sleep(2)
        
        elif opcao == "5":
            id_produto = int(input("Digite o id do produto a ser removido: "))
            if gerenciador_produto.remover(id_produto):
                print("Produto removido com sucesso!")
            else:
                print("Nenhum produto encontrado com esse id, ou erro na remoção.")
            time.sleep(2)
                
        elif opcao == "6":
            relatorio = gerenciador_produto.gerar_relatorio_produtos()
            print("\n--- RELATORIO ---")
            print(relatorio)
            time.sleep(15)
            
        elif opcao == "7":
            id_produto = int(input("Digite o id do produto a buscar: "))
            produto = gerenciador_produto.exibir_um(id_produto)
            if produto:
                print(produto)
            else:
                print("Produto não encontrado.")
            time.sleep(5)
                
        elif opcao == "8":
            break
            
        else:
            print("Opcao invalida!")
            time.sleep(2)
        limpar_terminal()
        
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
            # Cadastrar Cliente
            nome = input("Nome do Cliente: ").lower()
            telefone = input("Telefone: ").lower()
            email = input("Email: ").lower()
            endereco = input("Endereço: ").lower()
            cidade = input("Digite a cidade: ").lower()
            time_futebol = input("Digite o time de futebol: ").lower()
            assiste_one_piece = input("Assiste One Peace? [S/N] ").lower()
            if assiste_one_piece == "s":
                assiste_one_piece = True
            else:
                assiste_one_piece = False
            
        
            novo_cliente = Cliente(None, nome, telefone, email, endereco, cidade, time_futebol, assiste_one_piece)
            if gerenciador_cliente.inserir(novo_cliente):
                print("Cliente cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar Cliente.")
            time.sleep(5)

        elif opcao == "2":
            # Listar clientes
            clientes = gerenciador_cliente.listar_todos()
            print("\n--- LISTA DE CLIENTES ---")
            for cliente in clientes:
                print(cliente)
            time.sleep(2)
        
        elif opcao == "3":
            # Pesquisar por nome
            nome = input("Digite o nome para pesquisar: ")
            clientes = gerenciador_cliente.pesquisar_por_nome(nome)
            print("\n--- RESULTADO DA PESQUISA ---")
            for cliente in clientes:
                print(cliente)
            time.sleep(2)

        elif opcao == "4":
            # Alterar dados do cliente
            id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))

            print("Digite os novos dados do cliente:")
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            endereco = input("Novo endereco: ")

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
            time.sleep(2)
        
        elif opcao == "5":
            id_cliente = int(input("Digite o id do Cliente a ser removido: "))
            
            sucesso = gerenciador_cliente.remover(id_cliente)
            
            if sucesso:
                print("Cliente removido com sucesso!")
            else:
                print("Nenhum Cliente encontrado com esse id, ou erro na remoção.")  
            time.sleep(2)      
        
        elif opcao == "6":
            relatorio = gerenciador_cliente.gerar_relatorio_clientes()
            print("\n--- RELATORIO ---")
            print(relatorio)    
            time.sleep(15)        
        
        elif opcao == "7":
            id_cliente = int(input("Digite o id do cliente a buscar: "))
            print(gerenciador_cliente.exibir_um(id_cliente))
            time.sleep(5)
        
        elif opcao == "8":
            break
  
        else:
            print("Opcao invalida!")     
            time.sleep(5)
        
        limpar_terminal()
        
def menu_funcionarios():
    gerenciador_produto = GerenciadorProdutos()
    gerenciador_relatorios = GerenciadorRelatorios()

    while True:
        limpar_terminal()
        print("\n--- MENU DE FUNCIONÁRIO ---")
        print("1. Listar produtos com estoque baixo (< 5 unidades)")
        print("2. Gerar relatório mensal de vendas")
        print("3. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- PRODUTOS COM ESTOQUE BAIXO ---")
            produtos = gerenciador_produto.listar_produtos_com_estoque_baixo()
            if not produtos:
                print("Nenhum produto com estoque baixo encontrado.")
            else:
                for produto in produtos:
                    print(f"ID: {produto.id}, Nome: {produto.nome}, Estoque: {produto.quantidade_estoque}")
            time.sleep(10)
        
        elif opcao == "2":
            print("\n--- GERAR RELATÓRIO DE VENDAS ---")
            try:
                mes = int(input("Digite o mês (1-12): "))
                ano = int(input("Digite o ano (ex: 2025): "))
                if not (1 <= mes <= 12 and ano > 2000):
                    raise ValueError("Data inválida.")
                
                relatorio = gerenciador_relatorios.relatorio_vendas_vendedor(mes, ano)
                print(relatorio)
            except ValueError as e:
                print(f"Erro: {e}. Por favor, insira valores válidos.")
            time.sleep(15)

        elif opcao == "3":
            break
        
        else:
            print("Opção inválida!")
            time.sleep(2)

def main():
    while True:
        limpar_terminal()
        print("\n=== SISTEMA PAPELARIA ===")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Clientes")
        print("3. Funções de Funcionário") # NOVO
        print("4. Sair") # ALTERADO
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_clientes()
        elif opcao == "3": # NOVO
            menu_funcionarios()
        elif opcao == "4": # ALTERADO
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida!")
            time.sleep(2)

if __name__ == "__main__":
    main()