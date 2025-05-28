class Comercio:
    comerciantes:list = []

    def __init__(self, nome:str,produtos:list, vendedores:list):
        self.nome = nome
        self.produtos = produtos
        self.vendedores = vendedores

    def __str__(self):
        return f"Comercio: {self.nome} | Vendedores: {self.produtos}"

    def maior_venda(self, vendas:list):
        if not vendas:
            print("Não há vendas para comparar!")
            return

        maior_valor = max(vendas)
        indice_maior = vendas.index(maior_valor)
        vendedor_maior_venda = self.produtos[indice_maior]


        print(f"\nComparação de vendas:")
        for i, venda in enumerate(vendas):
            print(f"{i+1} - Vendedor: {self.vendedores[i]["Nome"]}: R${venda}")
            
        print(f"\nMaior venda: R${maior_valor}")
        print(f"Vendedor com maior venda: {self.vendedores[indice_maior]['Nome']}")
        print(vendedor_maior_venda)
