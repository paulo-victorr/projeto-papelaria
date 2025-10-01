import time
import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# Importações da biblioteca Rich para a interface
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text

# Importação das suas classes de gerenciador e modelo
from gerenciador_CRUD.gerenciador import GerenciadorProdutos, GerenciadorClientes, GerenciadorVendas, GerenciadorRelatorios, GerenciadorVendedores
from classes.produto import Produto
from classes.cliente import Cliente
from classes.venda import Venda
from classes.item_venda import ItemVenda
from classes.vendedor import Vendedor

# Inicializa o console do Rich para uma saída bonita
console = Console()

# --- FUNÇÕES AUXILIARES DE INTERFACE ---

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def imprimir_cabecalho(texto, cor="bold cyan"):
    limpar_terminal()
    console.print(Panel(Text(texto, justify="center", style="white"), style=cor, title_align="left"))

def aguardar_enter():
    Prompt.ask("\n[bold]Pressione Enter para continuar...[/bold]")

# --- MENUS DE GERENCIAMENTO (CRUD) ---

def menu_produtos():
    gerenciador_produto = GerenciadorProdutos()
    
    while True:
        imprimir_cabecalho("Gerenciar Produtos")
        menu = Table(show_header=False, box=None, padding=(0, 2))
        menu.add_column(style="magenta", justify="right")
        menu.add_column()
        menu.add_row("1", "Cadastrar Novo Produto")
        menu.add_row("2", "Listar Todos os Produtos")
        # Adicionar mais opções aqui se necessário
        menu.add_row("3", "Voltar")
        console.print(menu, justify="center")
        
        opcao = Prompt.ask("[bold]Escolha uma opção[/bold]", choices=["1", "2", "3"], default="3")
        
        if opcao == "1":
            imprimir_cabecalho("Cadastrar Novo Produto")
            try:
                nome = Prompt.ask("Nome do produto")
                categoria = Prompt.ask("Categoria")
                preco = float(Prompt.ask("Preço"))
                estoque = int(Prompt.ask("Quantidade em estoque"))
                fabricado_mari = Confirm.ask("É fabricado em Mari?")
                
                novo_produto = Produto(None, nome, categoria, preco, estoque, fabricado_mari)
                if gerenciador_produto.inserir(novo_produto):
                    console.print("\n:heavy_check_mark: [bold green]Produto cadastrado com sucesso![/bold green]")
                else:
                    console.print("\n:x: [bold red]Erro ao cadastrar produto.[/bold red]")
            except ValueError:
                console.print("\n:x: [bold red]Erro: Preço e estoque devem ser números.[/bold red]")
            time.sleep(2)
                
        elif opcao == "2":
            imprimir_cabecalho("Lista de Produtos")
            produtos = gerenciador_produto.listar_todos()
            tabela = Table(title="Produtos Cadastrados", expand=True, header_style="bold magenta")
            tabela.add_column("ID", style="cyan")
            tabela.add_column("Nome", style="white")
            tabela.add_column("Categoria", style="yellow")
            tabela.add_column("Preço", style="green", justify="right")
            tabela.add_column("Estoque", style="magenta", justify="right")
            tabela.add_column("Fab. Mari", style="blue", justify="center")

            for produto in produtos:
                tabela.add_row(
                    str(produto.id),
                    produto.nome,
                    produto.categoria,
                    f"R$ {produto.preco:.2f}",
                    str(produto.quantidade_estoque),
                    "Sim" if produto.fabricado_mari else "Não"
                )
            console.print(tabela)
            aguardar_enter()

        elif opcao == "3":
            break

def menu_clientes():
    gerenciador_cliente = GerenciadorClientes()
    
    while True:
        imprimir_cabecalho("Gerenciar Clientes")
        menu = Table(show_header=False, box=None, padding=(0, 2))
        menu.add_column(style="magenta", justify="right")
        menu.add_column()
        menu.add_row("1", "Cadastrar Novo Cliente")
        menu.add_row("2", "Listar Todos os Clientes")
        menu.add_row("3", "Voltar")
        console.print(menu, justify="center")

        opcao = Prompt.ask("[bold]Escolha uma opção[/bold]", choices=["1", "2", "3"], default="3")

        if opcao == "1":
            imprimir_cabecalho("Cadastrar Novo Cliente")
            nome = Prompt.ask("Nome do Cliente")
            telefone = Prompt.ask("Telefone")
            email = Prompt.ask("Email").lower()
            endereco = Prompt.ask("Endereço")
            cidade = Prompt.ask("Cidade").lower()
            time_futebol = Prompt.ask("Time de futebol").lower()
            assiste_one_piece = Confirm.ask("Assiste One Piece?")
            
            novo_cliente = Cliente(None, nome, telefone, email, endereco, cidade, time_futebol, assiste_one_piece)
            if gerenciador_cliente.inserir(novo_cliente):
                console.print("\n:heavy_check_mark: [bold green]Cliente cadastrado com sucesso![/bold green]")
            else:
                console.print("\n:x: [bold red]Erro ao cadastrar cliente.[/bold red]")
            time.sleep(2)

        elif opcao == "2":
            imprimir_cabecalho("Lista de Clientes")
            clientes = gerenciador_cliente.listar_todos()
            tabela = Table(title="Clientes Cadastrados", expand=True, header_style="bold magenta")
            tabela.add_column("ID", style="cyan")
            tabela.add_column("Nome", style="white")
            tabela.add_column("Telefone", style="yellow")
            tabela.add_column("Email", style="green")
            tabela.add_column("Cidade", style="magenta")
            
            for cliente in clientes:
                tabela.add_row(str(cliente.id), cliente.nome, cliente.telefone, cliente.email, cliente.cidade)
            console.print(tabela)
            aguardar_enter()

        elif opcao == "3":
            break

def menu_gerenciar_vendedores():
    gerenciador_vendedores = GerenciadorVendedores()

    while True:
        imprimir_cabecalho("Gerenciar Vendedores")
        menu = Table(show_header=False, box=None, padding=(0, 2))
        menu.add_column(style="magenta", justify="right")
        menu.add_column()
        menu.add_row("1", "Cadastrar Novo Vendedor")
        menu.add_row("2", "Listar Todos os Vendedores")
        menu.add_row("3", "Voltar")
        console.print(menu, justify="center")

        opcao = Prompt.ask("[bold]Escolha uma opção[/bold]", choices=["1", "2", "3"], default="3")

        if opcao == "1":
            imprimir_cabecalho("Cadastrar Novo Vendedor")
            nome = Prompt.ask("Nome do vendedor")
            email = Prompt.ask("Email do vendedor").lower()
            
            novo_vendedor = Vendedor(nome=nome, email=email)
            if gerenciador_vendedores.inserir(novo_vendedor):
                console.print("\n:heavy_check_mark: [bold green]Vendedor cadastrado com sucesso![/bold green]")
            else:
                console.print("\n:x: [bold red]Erro ao cadastrar vendedor.[/bold red]")
            time.sleep(2)

        elif opcao == "2":
            imprimir_cabecalho("Lista de Vendedores")
            vendedores = gerenciador_vendedores.listar_todos()
            tabela = Table(title="Vendedores Cadastrados", expand=True, header_style="bold magenta")
            tabela.add_column("ID", style="cyan")
            tabela.add_column("Nome", style="white")
            tabela.add_column("Email", style="green")
            if not vendedores:
                console.print("[yellow]Nenhum vendedor cadastrado.[/yellow]")
            else:
                for vendedor in vendedores:
                    tabela.add_row(str(vendedor.id), vendedor.nome, vendedor.email)
                console.print(tabela)
            aguardar_enter()

        elif opcao == "3":
            break
            
# --- MENUS DE OPERAÇÕES ---

def menu_vendas():
    imprimir_cabecalho("Realizar Nova Venda")
    gerenciador_clientes = GerenciadorClientes()
    gerenciador_vendedores = GerenciadorVendedores()
    gerenciador_produtos = GerenciadorProdutos()
    gerenciador_vendas = GerenciadorVendas()

    try:
        cliente_id = int(Prompt.ask("Digite o ID do Cliente"))
        cliente = gerenciador_clientes.exibir_um(cliente_id)
        if not cliente:
            console.print(":x: [bold red]Cliente não encontrado.[/bold red]")
            time.sleep(2)
            return

        vendedor_id = int(Prompt.ask("Digite o ID do Vendedor"))
        vendedores = gerenciador_vendedores.listar_todos()
        if not any(v.id == vendedor_id for v in vendedores):
            console.print(":x: [bold red]Vendedor não encontrado.[/bold red]")
            time.sleep(2)
            return
    except ValueError:
        console.print(":x: [bold red]ID inválido. Por favor, digite um número.[/bold red]")
        time.sleep(2)
        return
    
    console.print(f"\n[green]Cliente selecionado:[/] [bold]{cliente.nome}[/bold]")
    
    itens_carrinho = []
    while True:
        console.print("\nAdicionar produto ao carrinho (digite 'fim' para encerrar)")
        produto_id_str = Prompt.ask("Digite o ID do produto")
        if produto_id_str.lower() == 'fim':
            break
        
        try:
            produto_id = int(produto_id_str)
            produto = gerenciador_produtos.exibir_um(produto_id)
            if not produto:
                console.print(":x: [yellow]Produto não encontrado.[/yellow]")
                continue

            quantidade = int(Prompt.ask(f"Digite a quantidade de '[bold]{produto.nome}[/bold]'"))
            if quantidade <= 0:
                console.print(":x: [yellow]Quantidade deve ser positiva.[/yellow]")
                continue
            
            if quantidade > produto.quantidade_estoque:
                console.print(f":x: [yellow]Estoque insuficiente. Disponível: {produto.quantidade_estoque}[/yellow]")
                continue

            item = ItemVenda(produto_id=produto.id, quantidade=quantidade, preco_unitario=produto.preco)
            itens_carrinho.append(item)
            console.print(f":heavy_check_mark: [green]'{produto.nome}' adicionado ao carrinho.[/green]")

        except ValueError:
            console.print(":x: [red]Entrada inválida. Por favor, digite números para ID e quantidade.[/red]")

    if not itens_carrinho:
        console.print("\n:x: [yellow]Nenhum item no carrinho. Venda cancelada.[/yellow]")
        time.sleep(2)
        return

    imprimir_cabecalho("Resumo da Venda")
    tabela_resumo = Table(title="Itens no Carrinho", expand=True, header_style="bold magenta")
    tabela_resumo.add_column("Produto")
    tabela_resumo.add_column("Qtd", justify="right")
    tabela_resumo.add_column("Preço Unit.", justify="right")
    tabela_resumo.add_column("Subtotal", justify="right")

    for item in itens_carrinho:
        produto = gerenciador_produtos.exibir_um(item.produto_id)
        tabela_resumo.add_row(produto.nome, str(item.quantidade), f"R$ {item.preco_unitario:.2f}", f"R$ {item.calcular_subtotal():.2f}")

    console.print(tabela_resumo)

    valor_bruto = sum(item.calcular_subtotal() for item in itens_carrinho)
    desconto_percentual = cliente.calcular_desconto()
    valor_desconto = (valor_bruto * desconto_percentual) / 100
    valor_final = valor_bruto - valor_desconto

    console.print(f"\n[bold]Cliente:[/] {cliente.nome}")
    console.print(f"[bold]Valor Bruto:[/] R$ {valor_bruto:.2f}")
    if desconto_percentual > 0:
        console.print(f"[bold green]Desconto Aplicado ({desconto_percentual}%):[/] R$ {valor_desconto:.2f}")
    console.print(f"[bold cyan]Valor Final:[/] R$ {valor_final:.2f}")
    
    forma_pagamento = Prompt.ask("\nDigite a forma de pagamento", choices=["Cartao", "Pix", "Boleto", "Dinheiro", "Berries"], default="Cartao").upper()
    
    if Confirm.ask("\n[bold yellow]Confirmar a venda?[/bold yellow]"):
        venda = Venda(cliente_id=cliente.id, vendedor_id=vendedor_id, forma_pagamento=forma_pagamento)
        sucesso, mensagem = gerenciador_vendas.realizar_venda(venda, itens_carrinho)
        
        if sucesso:
            console.print(f"\n:tada: [bold green]{mensagem}[/bold green]")
        else:
            console.print(f"\n:x: [bold red]{mensagem}[/bold red]")
    else:
        console.print("\n:x: [yellow]Venda cancelada pelo usuário.[/yellow]")
        
    aguardar_enter()

def menu_cliente_consulta():
    imprimir_cabecalho("Área do Cliente")
    
    try:
        cliente_id = int(Prompt.ask("Para começar, por favor, digite seu ID de Cliente"))
    except ValueError:
        console.print(":x: [red]ID inválido. Por favor, digite apenas números.[/red]")
        time.sleep(2)
        return

    gerenciador_cliente = GerenciadorClientes()
    cliente = gerenciador_cliente.exibir_um(cliente_id)
    if not cliente:
        console.print(":x: [red]Cliente não encontrado com o ID fornecido.[/red]")
        time.sleep(2)
        return

    while True:
        imprimir_cabecalho(f"Bem-vindo(a), {cliente.nome}!")
        menu = Table(show_header=False, box=None, padding=(0, 2))
        menu.add_column(style="magenta", justify="right")
        menu.add_column()
        menu.add_row("1", "Ver meus dados cadastrais")
        menu.add_row("2", "Ver meu histórico de pedidos")
        menu.add_row("3", "Voltar")
        console.print(menu, justify="center")

        opcao = Prompt.ask("[bold]Escolha uma opção[/bold]", choices=["1", "2", "3"], default="3")

        if opcao == "1":
            imprimir_cabecalho("Seus Dados Cadastrais")
            painel_dados = (
                f"[bold cyan]ID:[/] {cliente.id}\n"
                f"[bold cyan]Nome:[/] {cliente.nome}\n"
                f"[bold cyan]Telefone:[/] {cliente.telefone}\n"
                f"[bold cyan]Email:[/] {cliente.email}\n"
                f"[bold cyan]Endereço:[/] {cliente.endereco}\n"
                f"[bold cyan]Cidade:[/] {cliente.cidade}\n"
                f"[bold cyan]Time:[/] {cliente.time_futebol}\n"
                f"[bold cyan]Assiste One Piece:[/] {'Sim' if cliente.assiste_one_piece else 'Não'}"
            )
            console.print(Panel(painel_dados, title="Dados Pessoais"))
            aguardar_enter()
        
        elif opcao == "2":
            imprimir_cabecalho("Seu Histórico de Pedidos")
            gerenciador_vendas = GerenciadorVendas()
            pedidos = gerenciador_vendas.listar_vendas_por_cliente(cliente_id)
            
            if not pedidos:
                console.print("[yellow]Você ainda não realizou nenhum pedido.[/yellow]")
            else:
                tabela_pedidos = Table(title="Histórico de Pedidos", expand=True, header_style="bold magenta")
                tabela_pedidos.add_column("ID Venda", style="cyan")
                tabela_pedidos.add_column("Data", style="white")
                tabela_pedidos.add_column("Valor Total", style="green", justify="right")
                tabela_pedidos.add_column("Status", style="yellow")
                
                for pedido in pedidos:
                    data_local = pedido.data_venda.astimezone(ZoneInfo("America/Sao_Paulo"))
                    tabela_pedidos.add_row(str(pedido.id), data_local.strftime('%d/%m/%Y %H:%M'), f"R$ {pedido.valor_total:.2f}", pedido.status_pagamento)
                console.print(tabela_pedidos)
            aguardar_enter()

        elif opcao == "3":
            break

def menu_funcionarios():
    gerenciador_produto = GerenciadorProdutos()
    gerenciador_relatorios = GerenciadorRelatorios()

    while True:
        imprimir_cabecalho("Painel do Funcionário")
        
        menu = Table(show_header=False, box=None, padding=(0, 2))
        menu.add_column(style="magenta", justify="right")
        menu.add_column()
        menu.add_row("1", "Gerenciar Vendedores (Funcionários)")
        menu.add_row("2", "Listar produtos com estoque baixo (< 5)")
        menu.add_row("3", "Gerar relatório mensal de vendas por vendedor")
        menu.add_row("4", "Ver relatório detalhado de todas as vendas (VIEW)")
        menu.add_row("5", "Reabastecer estoque de produto (Stored Procedure)")
        menu.add_row("6", "Voltar ao menu principal")
        console.print(menu, justify="center")

        opcao = Prompt.ask("\n[bold]Escolha uma opção[/bold]", choices=["1", "2", "3", "4", "5", "6"], default="6")

        if opcao == "1":
            menu_gerenciar_vendedores()

        elif opcao == "2":
            imprimir_cabecalho("Produtos com Estoque Baixo")
            produtos = gerenciador_produto.listar_produtos_com_estoque_baixo()
            
            if not produtos:
                console.print("[yellow]Nenhum produto com estoque baixo encontrado.[/yellow]")
            else:
                tabela_estoque = Table(title="Produtos com Estoque Crítico", expand=True, header_style="bold red")
                tabela_estoque.add_column("ID", style="cyan")
                tabela_estoque.add_column("Nome", style="white")
                tabela_estoque.add_column("Estoque Atual", style="red", justify="right")
                
                for produto in produtos:
                    tabela_estoque.add_row(str(produto.id), produto.nome, str(produto.quantidade_estoque))
                console.print(tabela_estoque)
            aguardar_enter()
        
        elif opcao == "3":
            imprimir_cabecalho("Relatório Mensal de Vendas por Vendedor")
            try:
                mes = int(Prompt.ask("Digite o mês (1-12)"))
                ano = int(Prompt.ask("Digite o ano (ex: 2025)"))
                if not (1 <= mes <= 12 and ano > 2000):
                    raise ValueError("Data inválida.")
                
                relatorio_str = gerenciador_relatorios.relatorio_vendas_vendedor(mes, ano)
                console.print(Panel(relatorio_str, title="Resultado", border_style="green"))

            except ValueError as e:
                console.print(f":x: [bold red]Erro: {e}. Por favor, insira valores válidos.[/bold red]")
            aguardar_enter()
        
        elif opcao == "4":
            imprimir_cabecalho("Relatório Detalhado de Vendas (VIEW)")
            vendas_detalhadas = gerenciador_relatorios.obter_relatorio_detalhado()
            
            if not vendas_detalhadas:
                console.print("[yellow]Nenhuma venda encontrada para exibir no relatório.[/yellow]")
            else:
                tabela_vendas = Table(title="Relatório Detalhado de Itens Vendidos", expand=True, header_style="bold magenta")
                tabela_vendas.add_column("ID Venda", style="cyan")
                tabela_vendas.add_column("Data (Local)", style="white")
                tabela_vendas.add_column("Cliente", style="yellow")
                tabela_vendas.add_column("Vendedor", style="blue")
                tabela_vendas.add_column("Produto", style="green")
                tabela_vendas.add_column("Qtd", style="magenta", justify="right")
                tabela_vendas.add_column("Subtotal", style="green", justify="right")

                for venda in vendas_detalhadas:
                    (venda_id, data_utc, cliente, cliente_cidade, vendedor, 
                     produto, qtd, preco_unitario, subtotal) = venda
                    
                    fuso_local = ZoneInfo("America/Sao_Paulo")
                    data_local = data_utc.astimezone(fuso_local)
                    
                    tabela_vendas.add_row(
                        str(venda_id),
                        data_local.strftime('%d/%m/%Y %H:%M'),
                        cliente,
                        vendedor,
                        produto,
                        str(qtd),
                        f"R$ {float(subtotal):.2f}"
                    )
                console.print(tabela_vendas)
            aguardar_enter()

        elif opcao == "5":
            imprimir_cabecalho("Reabastecer Estoque (Stored Procedure)")
            try:
                produto_id = int(Prompt.ask("Digite o ID do produto para reabastecer"))
                quantidade = int(Prompt.ask("Digite a quantidade a ser ADICIONADA"))

                if gerenciador_produto.reabastecer_estoque(produto_id, quantidade):
                    console.print(f"\n:heavy_check_mark: [bold green]Estoque do produto ID {produto_id} atualizado com sucesso![/bold green]")
                else:
                    console.print("\n:x: [bold red]Falha ao atualizar o estoque. Verifique o ID do produto.[/bold red]")

            except ValueError:
                console.print("\n:x: [bold red]Erro: ID do produto e quantidade devem ser números inteiros.[/bold red]")
            aguardar_enter()

        elif opcao == "6":
            break
# --- FUNÇÃO PRINCIPAL ---

def main():
    while True:
        imprimir_cabecalho("Sistema de Vendas da Papelaria", "bold green")
        
        menu_principal = Table(show_header=False, title="Menu Principal", box=None, padding=(0, 2))
        menu_principal.add_column(style="cyan", justify="right")
        menu_principal.add_column(style="bold")
        
        menu_principal.add_row("1", "Realizar Venda")
        menu_principal.add_row("2", "Área do Cliente")
        menu_principal.add_row("3", "Gerenciar Produtos")
        menu_principal.add_row("4", "Gerenciar Clientes")
        menu_principal.add_row("5", "Gerenciar Vendedores")
        menu_principal.add_row("6", "Painel do Funcionário (Relatórios)")
        menu_principal.add_row("7", "Sair")
        
        console.print(menu_principal, justify="center")
        
        opcao = Prompt.ask("\n[bold]Escolha uma opção[/bold]", choices=["1", "2", "3", "4", "5", "6", "7"], default="7")

        if opcao == "1":
            menu_vendas()
        elif opcao == "2":
            menu_cliente_consulta()
        elif opcao == "3":
            menu_produtos()
        elif opcao == "4":
            menu_clientes()
        elif opcao == "5":
            menu_gerenciar_vendedores()
        elif opcao == "6":
            menu_funcionarios()
        elif opcao == "7":
            if Confirm.ask("[bold yellow]Tem certeza que deseja sair?[/bold yellow]"):
                console.print("\nAté logo!", style="bold green")
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\nOperação cancelada pelo usuário. Até logo!", style="bold red")