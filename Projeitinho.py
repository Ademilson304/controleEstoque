# Renato
import os

os.system("cls")

BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'
class Moeda:
    def formatar(valor):
        return f"R${valor:,.2f}".replace(",", ".")

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='UTF8') as f:
            return f.readlines()
    except:
        return []

def salvar_arquivo(nome_arquivo, dados, sobrescrever=False):
    try:
        modo = 'w' if sobrescrever else 'a+'
        with open(nome_arquivo, modo, encoding='UTF8') as f:
            f.writelines(dados)
    except Exception as e:
        print(f"{RED}Erro ao salvar o arquivo: {e}{RESET}")

def gerar_codigo(arquivo):
    registros = carregar_arquivo(arquivo)
    if registros:
        ultimo_registro = registros[-1].split(";")[0]
        return str(int(ultimo_registro) + 1)
    return "1"

def cadastrar_produto():
    os.system("cls")
    produtos = carregar_arquivo('produtos.txt')
    codigo = gerar_codigo('produtos.txt')
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")

    while True:
        try:
            preco_compra = float(input("Preço de compra do produto: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para o preço de compra.{RESET}")
    
    while True:
        try:
            preco_venda = float(input("Preço de venda do produto: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para o preço de venda.{RESET}")

    produtos.append(f"{codigo};{nome};{descricao};{preco_compra};{preco_venda}\n")
    salvar_arquivo('produtos.txt', produtos, sobrescrever=True)
    print(f"{GREEN}Produto cadastrado com sucesso!{RESET}")


#Rai
def remover_produto():
    os.system("cls")
    codigo = input("Código do produto a ser removido: ")
    produtos = carregar_arquivo('produtos.txt')
    novo_produtos = [p for p in produtos if not p.startswith(codigo)]
    
    if len(produtos) == len(novo_produtos):
        print(f"{RED}Produto não encontrado.{RESET}")
    else:
        salvar_arquivo('produtos.txt', novo_produtos, sobrescrever=True)
        salvar_arquivo('compras.txt', [c for c in carregar_arquivo('compras.txt') if not c.startswith(codigo)], sobrescrever=True)
        salvar_arquivo('vendas.txt', [v for v in carregar_arquivo('vendas.txt') if not v.startswith(codigo)], sobrescrever=True)
        print(f"{GREEN}Produto e seus registros de compras e vendas removidos com sucesso.{RESET}")

def atualizar_produto():
    os.system("cls")
    codigo = input("Código do produto a ser atualizado: ")
    produtos = carregar_arquivo('produtos.txt')
    for i, produto in enumerate(produtos):
        if produto.startswith(codigo):
            nome = input("Novo nome do produto: ")
            descricao = input("Nova descrição do produto: ")
            
            while True:
                try:
                    preco_compra = float(input("Novo preço de compra: "))
                    break
                except:
                    print(f"{RED}Erro: Insira um valor numérico válido para o preço de compra.{RESET}")

            while True:
                try:
                    preco_venda = float(input("Novo preço de venda: "))
                    break
                except:
                    print(f"{RED}Erro: Insira um valor numérico válido para o preço de venda.{RESET}")
            
            produtos[i] = f"{codigo};{nome};{descricao};{preco_compra};{preco_venda}\n"
            salvar_arquivo('produtos.txt', produtos, sobrescrever=True)
            print(f"{GREEN}Produto atualizado com sucesso.{RESET}")
            return
    print(f"{RED}Produto não encontrado.{RESET}")

def comprar_produto():
    os.system("cls")
    codigo = input("Código do produto: ")
    produtos = carregar_arquivo('produtos.txt')

    if not any(produto.startswith(codigo) for produto in produtos):
        print(f"{RED}Erro: Produto não encontrado.{RESET}")
        return

    data_compra = input("Data da compra: ")
    codigo_compra = gerar_codigo('compras.txt')

    while True:
        try:
            quantidade = int(input("Quantidade comprada: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para a quantidade.{RESET}")

    compras = carregar_arquivo('compras.txt')
    compras.append(f"{codigo_compra};{codigo};{data_compra};{quantidade}\n")
    salvar_arquivo('compras.txt', compras, sobrescrever=True)
    print(f"{GREEN}Compra registrada com sucesso.{RESET}")

def vender_produto():
    os.system("cls")
    codigo = input("Código do produto a ser vendido: ")
    produtos = carregar_arquivo('produtos.txt')

    if not any(produto.startswith(codigo) for produto in produtos):
        print(f"{RED}Erro: Produto não encontrado.{RESET}")
        return

    data_venda = input("Data da venda: ")
    codigo_venda = gerar_codigo('vendas.txt')

    while True:
        try:
            quantidade = int(input("Quantidade a ser vendida: "))
            break
        except:
            print(f"{RED}Erro: Insira um valor numérico válido para a quantidade.{RESET}")

    compras = carregar_arquivo('compras.txt')
    vendas = carregar_arquivo('vendas.txt')

    qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
    qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)

    if quantidade > (qtd_comprada - qtd_vendida):
        print(f"{RED}Erro: Quantidade insuficiente para venda.{RESET}")
        return

    vendas.append(f"{codigo_venda};{codigo};{data_venda};{quantidade}\n")
    salvar_arquivo('vendas.txt', vendas, sobrescrever=True)
    print(f"{GREEN}Venda registrada com sucesso.{RESET}")


#Edemilson
def cancelar_compra():
    os.system("cls")
    codigo = input("Código da compra a ser cancelada: ")
    compras = carregar_arquivo('compras.txt')
    novas_compras = [compra for compra in compras if not compra.startswith(codigo)]
    if len(compras) == len(novas_compras):
        print(f"{RED}Compra não encontrada.{RESET}")
    else:
        salvar_arquivo('compras.txt', novas_compras, sobrescrever=True)
        print(f"{GREEN}Compra cancelada com sucesso.{RESET}")

def cancelar_venda():
    os.system("cls")
    codigo = input("Código da venda a ser cancelada: ")
    vendas = carregar_arquivo('vendas.txt')
    novas_vendas = [venda for venda in vendas if not venda.startswith(codigo)]
    if len(vendas) == len(novas_vendas):
        print(f"{RED}Venda não encontrada.{RESET}")
    else:
        salvar_arquivo('vendas.txt', novas_vendas, sobrescrever=True)
        print(f"{GREEN}Venda cancelada com sucesso.{RESET}")

def listar_produtos():
    os.system("cls")
    produtos = carregar_arquivo('produtos.txt')
    compras = carregar_arquivo('compras.txt')
    vendas = carregar_arquivo('vendas.txt')
    
    if produtos:
        print(f"{YELLOW}Produtos cadastrados:\n{RESET}")
        for produto in produtos:
            codigo, nome, descricao, preco_compra, preco_venda = produto.strip().split(";")
            qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
            qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)
            preco_compra_formatado = Moeda.formatar(float(preco_compra))
            preco_venda_formatado = Moeda.formatar(float(preco_venda))
            
            print(f"{YELLOW}Código: {codigo}{RESET}")
            print(f"Nome: {nome}")
            print(f"Descrição: {descricao}")
            print(f"Preço Compra: {preco_compra_formatado}")
            print(f"Preço Venda: {preco_venda_formatado}")
            print(f"Quantidade Comprada: {qtd_comprada}")
            print(f"Quantidade Vendida: {qtd_vendida}\n")
    else:
        print(f"{RED}Nenhum produto cadastrado.{RESET}")

def detalhar_produto():
    os.system("cls")
    codigo = input("Código do produto: ")
    print("\n")
    produtos = carregar_arquivo('produtos.txt')
    compras = carregar_arquivo('compras.txt')
    vendas = carregar_arquivo('vendas.txt')

    for produto in produtos:
        if produto.startswith(codigo):
            codigo, nome, descricao, preco_compra, preco_venda = produto.strip().split(";")
            qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
            qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)
            valor_investido = qtd_comprada * float(preco_compra)
            valor_arrecadado = qtd_vendida * float(preco_venda)
            lucro = valor_arrecadado - valor_investido
            
            print(f"{YELLOW}Código do produto: {codigo}{RESET}")
            print(f"Nome do produto: {nome}")
            print(f"Descrição do produto: {descricao}")
            print(f"Preço de compra do produto: {Moeda.formatar(float(preco_compra))}")
            print(f"Preço de venda do produto: {Moeda.formatar(float(preco_venda))}")
            print(f"Quantidade Comprada: {qtd_comprada}")
            print(f"Quantidade Vendida: {qtd_vendida}")
            print(f"Valor total investido: {Moeda.formatar(valor_investido)}")
            print(f"Valor total arrecadado: {Moeda.formatar(valor_arrecadado)}")
            print(f"Lucro: {Moeda.formatar(lucro)}\n")

            print("Compras do produto:")
            for compra in compras:
                if compra.split(";")[1] == codigo:
                    print(f"  {compra.strip()}")

            print("\nVendas do produto:")
            for venda in vendas:
                if venda.split(";")[1] == codigo:
                    print(f"  {venda.strip()}")
            return
    print(f"{RED}Produto não encontrado.{RESET}")


#Raysa
def saldo_financeiro():
    os.system("cls")
    produtos = carregar_arquivo('produtos.txt')
    compras = carregar_arquivo('compras.txt')
    vendas = carregar_arquivo('vendas.txt')

    total_investido = 0
    total_arrecadado = 0

    for produto in produtos:
        codigo, nome, descricao, preco_compra, preco_venda = produto.strip().split(";")
        qtd_comprada = sum(int(c.split(";")[3]) for c in compras if c.split(";")[1] == codigo)
        qtd_vendida = sum(int(v.split(";")[3]) for v in vendas if v.split(";")[1] == codigo)
        total_investido += qtd_comprada * float(preco_compra)
        total_arrecadado += qtd_vendida * float(preco_venda)
    
    lucro_total = total_arrecadado - total_investido
    print(f"{YELLOW}Total investido: {Moeda.formatar(total_investido)}{RESET}")
    print(f"{YELLOW}Total arrecadado: {Moeda.formatar(total_arrecadado)}{RESET}")
    print(f"{YELLOW}Lucro total: {Moeda.formatar(lucro_total)}{RESET}")

def autenticar():
    senha = "1"
    tentativa = input(f"{YELLOW}Digite a senha para acessar o sistema: {RESET}")
    if tentativa == senha:
        return True
    else:
        print(f"{RED}Senha incorreta. Acesso negado.{RESET}")
        return False

def menu():
    if not autenticar():
        return
    
    while True:
        os.system("cls")
        frase = "Escolha uma opção"
        print(f"{YELLOW}┌─{'─' * 18}{frase.upper()}{'─' * 20}─┐{RESET}")
        print(f"{YELLOW}│ ┌─{'─' * 51}─┐ │{RESET}")
        print(f"{YELLOW}│ │ 1 - Cadastrar Produto          2 - Comprar Produto  │ │{RESET}")
        print(f"{YELLOW}│ │ 3 - Vender Produto             4 - Listar Produtos  │ │{RESET}")
        print(f"{YELLOW}│ │ 5 - Detalhar Produto           6 - Remover Produto  │ │{RESET}")
        print(f"{YELLOW}│ │ 7 - Atualizar Produto          8 - Cancelar Compra  │ │{RESET}")
        print(f"{YELLOW}│ │ 9 - Cancelar Venda            10 - Saldo Financeiro │ │{RESET}")
        print(f"{YELLOW}│ │ 11 - Sair                                           │ │{RESET}")
        print(f"{YELLOW}│ └─{'─' * 51}─┘ │{RESET}")
        print(f"{YELLOW}└─{'─' * 55}─┘{RESET}")

        opcao = input(f"{YELLOW}Digite sua escolha: {RESET}")

        if opcao == "1":
            cadastrar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "2":
            comprar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "3":
            vender_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "4":
            listar_produtos()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "5":
            detalhar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "6":
            remover_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "7":
            atualizar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "8":
            cancelar_compra()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "9":
            cancelar_venda()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "10":
            saldo_financeiro()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "11":
            os.system("cls")
            print("Saindo...")
            break
        else:
            print(f"{RED}Opção inválida! Tente novamente.{RESET}")

menu()
