from gerenciador_CRUD.gerenciador import GerenciadorProdutos, GerenciadorClientes, GerenciadorVendas, GerenciadorRelatorios, GerenciadorVendedores
from classes.produto import Produto
from classes.cliente import Cliente
from classes.venda import Venda
from classes.item_venda import ItemVenda
from classes.vendedor import Vendedor
import time
import os  

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def menu_produtos():
    gerenciador_produto = GerenciadorProdutos()
    
    while True:
        limpar_terminal()
        print("\n--- GERENCIAR PRODUTOS ---")
        print("1. Cadastrar novo produto")
        print("2. Listar todos os produtos")
        print("3. Pesquisar produtos (filtros)")
        print("4. Alterar produto")
        print("5. Remover produto")
        print("6. Gerar relatório de produtos")
        print("7. Buscar por ID")
        print("8. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").lower()
        
        if opcao == "1":
            try:
                print("\n--- CADASTRO DE NOVO PRODUTO ---")
                nome = input("Nome do produto: ")
                categoria = input("Categoria: ")
                preco = float(input("Preço: "))
                estoque = int(input("Quantidade em estoque: "))
                fabricado_mari_str = input("É fabricado em Mari? (s/n): ").lower()
                fabricado_mari = True if fabricado_mari_str == 's' else False
                
                novo_produto = Produto(None, nome, categoria, preco, estoque, fabricado_mari)
                if gerenciador_produto.inserir(novo_produto):
                    print("Produto cadastrado com sucesso!")
                else:
                    print("Erro ao cadastrar produto.")
            except ValueError:
                print("Erro: Preço e estoque devem ser números.")
            time.sleep(2)
                
        elif opcao == "2":
            produtos = gerenciador_produto.listar_todos()
            print("\n--- LISTA DE PRODUTOS ---")
            for produto in produtos:
                print(produto)
            input("\nPressione Enter para continuar...")
                
        elif opcao == "3":
            while True:
                limpar_terminal()
                print("\n--- MENU DE PESQUISA DE PRODUTOS ---")
                print("1. Pesquisar por nome")
                print("2. Pesquisar por categoria")
                print("3. Pesquisar por faixa de preço")
                print("4. Listar fabricados em Mari")
                print("5. Voltar")
                
                sub_opcao = input("Escolha o tipo de pesquisa: ").lower()
                
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
                input("\nPressione Enter para continuar...")
        
        elif opcao == "4":
            try:
                id_produto = int(input("Digite o ID do produto que deseja alterar: "))
                produto_existente = gerenciador_produto.exibir_um(id_produto)
                if not produto_existente:
                    print("Produto não encontrado.")
                    time.sleep(2)
                    continue
                
                print("\nDigite os novos dados (deixe em branco para manter o valor atual):")
                nome = input(f"Novo nome ({produto_existente.nome}): ") or produto_existente.nome
                categoria = input(f"Nova categoria ({produto_existente.categoria}): ") or produto_existente.categoria
                preco_str = input(f"Novo preço ({produto_existente.preco}): ")
                preco = float(preco_str) if preco_str else produto_existente.preco
                estoque_str = input(f"Nova quantidade ({produto_existente.quantidade_estoque}): ")
                estoque = int(estoque_str) if estoque_str else produto_existente.quantidade_estoque
                fabricado_mari_str = input(f"Fabricado em Mari? (s/n) ({'s' if produto_existente.fabricado_mari else 'n'}): ").lower()
                fabricado_mari = (True if fabricado_mari_str == 's' else False) if fabricado_mari_str else produto_existente.fabricado_mari

                produto_atualizado = Produto(id_produto, nome, categoria, preco, estoque, fabricado_mari)
                if gerenciador_produto.alterar(id_produto, produto_atualizado):
                    print("Produto alterado com sucesso!")
                else:
                    print("Erro ao alterar produto.")
            except ValueError:
                print("Erro: O ID do produto deve ser um número.")
            time.sleep(2)
        
        elif opcao == "5":
            try:
                id_produto = int(input("Digite o ID do produto a ser removido: "))
                if gerenciador_produto.remover(id_produto):
                    print("Produto removido com sucesso!")
                else:
                    print("Nenhum produto encontrado com esse ID, ou erro na remoção.")
            except ValueError:
                print("Erro: O ID do produto deve ser um número.")
            time.sleep(2)
                
        elif opcao == "6":
            relatorio = gerenciador_produto.gerar_relatorio_produtos()
            print("\n--- RELATÓRIO DE PRODUTOS ---")
            print(relatorio)
            input("\nPressione Enter para continuar...")
            
        elif opcao == "7":
            try:
                id_produto = int(input("Digite o ID do produto a buscar: "))
                produto = gerenciador_produto.exibir_um(id_produto)
                if produto:
                    print(produto)
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Erro: O ID do produto deve ser um número.")
            time.sleep(5)
                
        elif opcao == "8":
            break
            
        else:
            print("Opção inválida!")
            time.sleep(2)

def menu_clientes():
    gerenciador_cliente = GerenciadorClientes()
    
    while True:
        limpar_terminal()
        print("\n--- GERENCIAR CLIENTES ---")
        print("1. Cadastrar novo cliente")
        print("2. Listar todos os clientes")
        print("3. Pesquisar cliente por nome")
        print("4. Alterar dados do cliente")
        print("5. Remover cliente")
        print("6. Gerar relatório de clientes")
        print("7. Buscar por ID")
        print("8. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").lower()
    
        if opcao == "1":
            print("\n--- CADASTRO DE NOVO CLIENTE ---")
            nome = input("Nome do Cliente: ")
            telefone = input("Telefone: ")
            email = input("Email: ").lower()
            endereco = input("Endereço: ")
            cidade = input("Cidade: ").lower()
            time_futebol = input("Time de futebol: ").lower()
            assiste_one_piece_str = input("Assiste One Piece? [S/N] ").lower()
            assiste_one_piece = True if assiste_one_piece_str == "s" else False
            
            novo_cliente = Cliente(None, nome, telefone, email, endereco, cidade, time_futebol, assiste_one_piece)
            if gerenciador_cliente.inserir(novo_cliente):
                print("Cliente cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar Cliente.")
            time.sleep(3)

        elif opcao == "2":
            clientes = gerenciador_cliente.listar_todos()
            print("\n--- LISTA DE CLIENTES ---")
            for cliente in clientes:
                print(cliente)
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":
            nome = input("Digite o nome para pesquisar: ")
            clientes = gerenciador_cliente.pesquisar_por_nome(nome)
            print("\n--- RESULTADO DA PESQUISA ---")
            for cliente in clientes:
                print(cliente)
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            try:
                id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))
                cliente_existente = gerenciador_cliente.exibir_um(id_cliente)
                if not cliente_existente:
                    print("Cliente não encontrado.")
                    time.sleep(2)
                    continue

                print("\nDigite os novos dados (deixe em branco para manter o valor atual):")
                nome = input(f"Novo nome ({cliente_existente.nome}): ") or cliente_existente.nome
                telefone = input(f"Novo telefone ({cliente_existente.telefone}): ") or cliente_existente.telefone
                email = input(f"Novo email ({cliente_existente.email}): ").lower() or cliente_existente.email
                endereco = input(f"Novo endereço ({cliente_existente.endereco}): ") or cliente_existente.endereco
                cidade = input(f"Nova cidade ({cliente_existente.cidade}): ").lower() or cliente_existente.cidade
                time_futebol = input(f"Novo time ({cliente_existente.time_futebol}): ").lower() or cliente_existente.time_futebol
                one_piece_str = input(f"Assiste One Piece? (s/n) ({'s' if cliente_existente.assiste_one_piece else 'n'}): ").lower()
                assiste_one_piece = (True if one_piece_str == 's' else False) if one_piece_str else cliente_existente.assiste_one_piece
                
                cliente_atualizado = Cliente(id_cliente, nome, telefone, email, endereco, cidade, time_futebol, assiste_one_piece)

                if gerenciador_cliente.alterar(id_cliente, cliente_atualizado):
                    print("Cliente alterado com sucesso!")
                else:
                    print("Erro ao alterar cliente.")
            except ValueError:
                print("Erro: O ID do cliente deve ser um número.")
            time.sleep(2)
        
        elif opcao == "5":
            try:
                id_cliente = int(input("Digite o ID do cliente a ser removido: "))
                if gerenciador_cliente.remover(id_cliente):
                    print("Cliente removido com sucesso!")
                else:
                    print("Nenhum cliente encontrado com esse ID, ou erro na remoção.")
            except ValueError:
                print("Erro: O ID do cliente deve ser um número.")
            time.sleep(2)      
        
        elif opcao == "6":
            relatorio = gerenciador_cliente.gerar_relatorio_clientes()
            print("\n--- RELATÓRIO DE CLIENTES ---")
            print(relatorio)    
            input("\nPressione Enter para continuar...")     
        
        elif opcao == "7":
            try:
                id_cliente = int(input("Digite o ID do cliente a buscar: "))
                cliente = gerenciador_cliente.exibir_um(id_cliente)
                if cliente:
                    print(cliente)
                else:
                    print("Cliente não encontrado.")
            except ValueError:
                print("Erro: O ID do cliente deve ser um número.")
            time.sleep(5)
        
        elif opcao == "8":
            break
  
        else:
            print("Opção inválida!")     
            time.sleep(2)

def menu_gerenciar_vendedores():
    gerenciador_vendedores = GerenciadorVendedores()

    while True:
        limpar_terminal()
        print("\n--- GERENCIAR VENDEDORES ---")
        print("1. Cadastrar novo vendedor")
        print("2. Listar todos os vendedores")
        print("3. Voltar ao Menu de Funcionário")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == "1":
            print("\n--- CADASTRO DE NOVO VENDEDOR ---")
            nome = input("Nome do vendedor: ")
            email = input("Email do vendedor: ").lower()
            
            novo_vendedor = Vendedor(nome=nome, email=email)
            if gerenciador_vendedores.inserir(novo_vendedor):
                print("Vendedor cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar vendedor.")
            time.sleep(3)

        elif opcao == "2":
            print("\n--- LISTA DE VENDEDORES ---")
            vendedores = gerenciador_vendedores.listar_todos()
            if not vendedores:
                print("Nenhum vendedor cadastrado.")
            else:
                for vendedor in vendedores:
                    print(vendedor)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            break
        else:
            print("Opção inválida!")
            time.sleep(2)

def menu_funcionarios():
    gerenciador_produto = GerenciadorProdutos()
    gerenciador_relatorios = GerenciadorRelatorios()

    while True:
        limpar_terminal()
        print("\n--- MENU DE FUNCIONÁRIO ---")
        print("1. Gerenciar Vendedores (Funcionários)")
        print("2. Listar produtos com estoque baixo (< 5 unidades)")
        print("3. Gerar relatório mensal de vendas por vendedor")
        print("4. Ver relatório detalhado de todas as vendas")
        print("5. Reabastecer estoque de produto")
        print("6. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == "1":
            menu_gerenciar_vendedores()
        elif opcao == "2":
            print("\n--- PRODUTOS COM ESTOQUE BAIXO ---")
            produtos = gerenciador_produto.listar_produtos_com_estoque_baixo()
            if not produtos:
                print("Nenhum produto com estoque baixo encontrado.")
            else:
                for produto in produtos:
                    print(f"ID: {produto.id}, Nome: {produto.nome}, Estoque: {produto.quantidade_estoque}")
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":
            print("\n--- GERAR RELATÓRIO DE VENDAS POR VENDEDOR ---")
            try:
                mes = int(input("Digite o mês (1-12): "))
                ano = int(input("Digite o ano (ex: 2025): "))
                if not (1 <= mes <= 12 and ano > 2000):
                    raise ValueError("Data inválida.")
                
                relatorio = gerenciador_relatorios.relatorio_vendas_vendedor(mes, ano)
                print(relatorio)
            except ValueError as e:
                print(f"Erro: {e}. Por favor, insira valores válidos.")
            input("\nPressione Enter para continuar...")
        
        elif opcao == "4":
            print("\n--- RELATÓRIO DETALHADO DE VENDAS ---")
            vendas_detalhadas = gerenciador_relatorios.obter_relatorio_detalhado()
            if not vendas_detalhadas:
                print("Nenhuma venda encontrada.")
            else:
                print(f"{'ID Venda':<10} | {'Data':<20} | {'Cliente':<25} | {'Vendedor':<25} | {'Produto':<25} | {'Qtd':<5} | {'Subtotal':<10}")
                print("-" * 130)
                for venda in vendas_detalhadas:
                    venda_id, data, cliente, vendedor, produto, qtd, _, subtotal = venda
                    data_formatada = data.strftime('%d/%m/%Y %H:%M')
                    subtotal_formatado = f"R${float(subtotal):.2f}"
                    print(f"{str(venda_id):<10} | {data_formatada:<20} | {cliente:<25} | {vendedor:<25} | {produto:<25} | {str(qtd):<5} | {subtotal_formatado:<10}")
            input("\nPressione Enter para continuar...")

        elif opcao == "5":
            print("\n--- REABASTECER ESTOQUE ---")
            try:
                produto_id = int(input("Digite o ID do produto para reabastecer: "))
                quantidade = int(input("Digite a quantidade a ser ADICIONADA: "))
                if gerenciador_produto.reabastecer_estoque(produto_id, quantidade):
                    print("\nEstoque atualizado com sucesso!")
                else:
                    print("\nFalha ao atualizar o estoque. Verifique os dados e o log de erro.")
            except ValueError:
                print("\nErro: ID do produto e quantidade devem ser números inteiros.")
            input("\nPressione Enter para continuar...")

        elif opcao == "6":
            break
        
        else:
            print("Opção inválida!")
            time.sleep(2)

def menu_cliente_consulta():
    limpar_terminal()
    print("\n--- ÁREA DO CLIENTE ---")
    
    try:
        cliente_id = int(input("Para começar, por favor, digite seu ID de Cliente: "))
    except ValueError:
        print("ID inválido. Por favor, digite apenas números.")
        time.sleep(3)
        return

    gerenciador_cliente = GerenciadorClientes()
    gerenciador_vendas = GerenciadorVendas()

    cliente = gerenciador_cliente.exibir_um(cliente_id)
    if not cliente:
        print("Cliente não encontrado com o ID fornecido.")
        time.sleep(3)
        return

    while True:
        limpar_terminal()
        print(f"\nBem-vindo(a), {cliente.nome}!")
        print("O que você gostaria de fazer?")
        print("1. Ver meus dados cadastrais")
        print("2. Ver meu histórico de pedidos")
        print("3. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == "1":
            print("\n--- SEUS DADOS CADASTRAIS ---")
            print(f"ID: {cliente.id}")
            print(f"Nome: {cliente.nome}")
            print(f"Telefone: {cliente.telefone}")
            print(f"Email: {cliente.email}")
            print(f"Endereço: {cliente.endereco}")
            print(f"Cidade: {cliente.cidade}")
            print(f"Time: {cliente.time_futebol}")
            print(f"Assiste One Piece: {'Sim' if cliente.assiste_one_piece else 'Não'}")
            input("\nPressione Enter para continuar...")
        
        elif opcao == "2":
            print("\n--- SEU HISTÓRICO DE PEDIDOS ---")
            pedidos = gerenciador_vendas.listar_vendas_por_cliente(cliente_id)
            
            if not pedidos:
                print("Você ainda não realizou nenhum pedido.")
            else:
                for pedido in pedidos:
                    print(pedido)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            break
        else:
            print("Opção inválida!")
            time.sleep(2)

def menu_vendas():
    limpar_terminal()
    print("\n--- REALIZAR NOVA VENDA ---")

    gerenciador_clientes = GerenciadorClientes()
    gerenciador_vendedores = GerenciadorVendedores()
    gerenciador_produtos = GerenciadorProdutos()
    gerenciador_vendas = GerenciadorVendas()

    try:
        cliente_id = int(input("Digite o ID do Cliente: "))
        cliente = gerenciador_clientes.exibir_um(cliente_id)
        if not cliente:
            print("Cliente não encontrado.")
            time.sleep(2)
            return

        vendedor_id = int(input("Digite o ID do Vendedor: "))
        vendedores = gerenciador_vendedores.listar_todos()
        if not any(v.id == vendedor_id for v in vendedores):
            print("Vendedor não encontrado.")
            time.sleep(2)
            return
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        time.sleep(2)
        return
    
    print(f"\nCliente: {cliente.nome}")
    print("-" * 30)

    itens_carrinho = []
    while True:
        print("\nAdicionar produto ao carrinho (digite 'fim' para encerrar)")
        try:
            produto_id_str = input("Digite o ID do produto: ")
            if produto_id_str.lower() == 'fim':
                break
            
            produto_id = int(produto_id_str)
            produto = gerenciador_produtos.exibir_um(produto_id)
            if not produto:
                print("Produto não encontrado.")
                continue

            quantidade = int(input(f"Digite a quantidade de '{produto.nome}': "))
            if quantidade <= 0:
                print("Quantidade deve ser positiva.")
                continue
            
            if quantidade > produto.quantidade_estoque:
                print(f"Estoque insuficiente. Disponível: {produto.quantidade_estoque}")
                continue

            item = ItemVenda(produto_id=produto.id, quantidade=quantidade, preco_unitario=produto.preco)
            itens_carrinho.append(item)
            print(f"'{produto.nome}' adicionado ao carrinho.")

        except ValueError:
            print("Entrada inválida. Por favor, digite números para ID e quantidade.")

    if not itens_carrinho:
        print("Nenhum item no carrinho. Venda cancelada.")
        time.sleep(2)
        return

    limpar_terminal()
    print("\n--- RESUMO DA VENDA ---")
    valor_bruto = sum(item.calcular_subtotal() for item in itens_carrinho)
    print(f"Cliente: {cliente.nome}")
    print(f"Total de itens: {len(itens_carrinho)}")
    print(f"Valor bruto: R$ {valor_bruto:.2f}")

    desconto_percentual = cliente.calcular_desconto()
    if desconto_percentual > 0:
        print(f"Desconto aplicável: {desconto_percentual}%")

    print("-" * 30)
    forma_pagamento = input("Digite a forma de pagamento (Cartao, Pix, Boleto, Dinheiro): ").upper()
    
    confirmacao = input("Confirmar a venda? (s/n): ").lower()
    if confirmacao == 's':
        venda = Venda(cliente_id=cliente.id, vendedor_id=vendedor_id, forma_pagamento=forma_pagamento)
        
        sucesso, mensagem = gerenciador_vendas.realizar_venda(venda, itens_carrinho)
        
        print(mensagem)
    else:
        print("Venda cancelada pelo usuário.")
        
    input("\nPressione Enter para voltar ao menu principal...")

def main():
    while True:
        limpar_terminal()
        print("\n=== SISTEMA PAPELARIA ===")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Clients")
        print("3. Funções de Funcionário")
        print("4. Área do Cliente")
        print("5. Realizar Venda")
        print("6. Sair")
        
        opcao = input("Escolha uma opcao: ").lower()
        
        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_clientes()
        elif opcao == "3":
            menu_funcionarios()
        elif opcao == "4":
            menu_cliente_consulta()
        elif opcao == "5":
            menu_vendas()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida!")
            time.sleep(2)

if __name__ == "__main__":
    main()