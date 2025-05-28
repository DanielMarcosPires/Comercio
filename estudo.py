import re #Para eu poder usar o RegEx
from Comercio.comercio import Comercio
from Comercio.produto import Produto
from Comercio.vendedor import Vendedor
import os
vendedores = []
produtos = []

def adicionar_vendedor():
    os.system("cls")
    print("\n=== Adicionar Vendedor ===")
    nome = input("Nome do vendedor: ")
    empresa = input("Empresa do vendedor: ")
    
    if re.search(r'\d', nome) or re.search(r'\d', empresa): #Verifica se o nome ou empresa contem números
        print("Erro: Nome ou empresa inválidos! Não podem conter números.")
        return None
    
    vendedor = Vendedor(nome, empresa)

    vendedores.append(vendedor)

    print(vendedor.mostrar_vendedor())
    print("Vendedor adicionado com sucesso!")
    return vendedor

def adicionar_produto():
    os.system("cls")
    if not vendedores:
        print("Erro: Não há vendedores cadastrados. Cadastre um vendedor primeiro!")
        return None
    
    print("\n=== Vendedores Disponíveis ===")
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor.mostrar_vendedor()}")
    
    try:
        escolha = int(input("\nEscolha o número do vendedor para este produto: ")) - 1
        if escolha < 0 or escolha >= len(vendedores):
            print("Erro: Número de vendedor inválido!")
            return None
        
        vendedor_escolhido = vendedores[escolha]
        
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        marca = input("Empresa do produto: ")
        
        if re.search(r'\d', nome) or re.search(r'\d', marca):
            print("Erro: Nome ou marca inválidos! Não podem conter números.")
            return None

        produto = Produto(nome, preco, marca)
        produtos.append(produto)
        
        vendedor_escolhido.adicionar_produto(produto.extrair_dados())
        
        print(f"Produto adicionado com sucesso ao vendedor {vendedor_escolhido._name}!")
        return produto
    except ValueError:
        print("Erro: Por favor, digite um número válido!")
        return None

def mostrar_produtos():
    os.system("cls")
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    print("\n=== Lista de Produtos por Vendedor ===")
    
    for vendedor in vendedores:
        print(f"\nVendedor: {vendedor._name}")
        produtos_vendedor = vendedor.mostrar_produtos()
       
        if produtos_vendedor:
            for produto in produtos_vendedor:
                print(f"- Nome: {produto['nome_do_produto']}, Preço: R${produto['price']}, Marca: {produto['marca']}")
        else:
            print("Nenhum produto cadastrado para este vendedor.")

def mostrar_vendedores():
    os.system("cls")
    if not vendedores:
        print("Nenhum vendedor cadastrado!")
        return
    
    print("\n=== Lista de Vendedores ===")
    
    for i, vendedor in enumerate(vendedores, 1):
        print(f"{i}. {vendedor.mostrar_vendedor()}")

def mostrar_maior_venda():
    os.system("cls")
    if not vendedores:
        print("Não há vendedores cadastrados!")
        return
    
    print("\n=== Análise de Vendas ===")
    # Calcula o total de vendas para cada vendedor
    totais = []
    for vendedor in vendedores:
        total = vendedor.preco_total()
        totais.append(total)
        print(f"Total de vendas de {vendedor._name}: R${total}")
    
    # Cria instância do comércio com os dados atuais
    comercio = Comercio("Procon",
        [v.mostrar_produtos() for v in vendedores],
        [v.mostrar_vendedor() for v in vendedores]
    )
    
    # Mostra quem vendeu mais
    comercio.maior_venda(totais)

print(
    """
   
█▄▄ █▀▀ █▀▄▀█   █░█ █ █▄░█ █▀▄ █▀█ █
█▄█ ██▄ █░▀░█   ▀▄▀ █ █░▀█ █▄▀ █▄█ ▄
    """
)

while True:
    controle = input("\nDeseja continuar? (s/n): ")
    if controle.lower() == "s":
        print("\n=== Menu Principal ===")
        controle = input("1 - Adicionar vendedor\n2 - Adicionar produto\n3 - Mostrar produtos\n4 - Mostrar vendedores\n5 - Mostrar maior venda\n6 - Sair\nEscolha uma opção: ")
        match controle:
            case "1": adicionar_vendedor()
            case "2": adicionar_produto()
            case "3": mostrar_produtos()
            case "4": mostrar_vendedores()
            case "5": mostrar_maior_venda()
            case "6":
                print("Aplicação finalizada!")
                break
            case _:
                print("Opção inválida!")
    else:
        print("Aplicação finalizada!")
        break

#===================Código antigo=========================== 

# vendedor1 = Vendedor(name="Daniel",empresa="Teste")

# produto1 = Produto("apple", 200, "Fazenda")
# produto2 = Produto("Banana", 100, "Fazenda")
# produto3 = Produto("Pera", 150, "Fazenda")

# vendedor1.adicionar_produto(produto1.extrair_dados())

# vendedor2 = Vendedor(name="Bruno", empresa="Mercado")
# vendedor2.adicionar_produto(produto2.extrair_dados())

# vendedor3 = Vendedor(name="João", empresa="Mercado")
# vendedor3.adicionar_produto(produto3.extrair_dados())

# total = vendedor1.preco_total()
# total2 = vendedor2.preco_total()
# total3 = vendedor3.preco_total()

# comercio = Comercio("Procon", 
#     [vendedor1.mostrar_produtos(), vendedor2.mostrar_produtos(), vendedor3.mostrar_produtos()], 
#     [vendedor1.mostrar_vendedor(), vendedor2.mostrar_vendedor(), vendedor3.mostrar_vendedor()]
# )

# comercio.maior_venda([total, total2, total3])