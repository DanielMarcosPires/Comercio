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
        indices_maiores = [i for i, v in enumerate(vendas) if v == maior_valor]
        
        print(f"\nComparação de vendas:")
        for i, venda in enumerate(vendas):
            print(f"{i+1} - Vendedor: {self.vendedores[i]['Nome']}: R${venda}")
            
        print(f"\nMaior venda: R${maior_valor}")
        
        if len(indices_maiores) > 1:
            print("Houve empate entre os vendedores:")
            for indice in indices_maiores:
                print(f"- {self.vendedores[indice]['Nome']}")
                print(self.produtos[indice])
        else:
            print(f"Vendedor com maior venda: {self.vendedores[indices_maiores[0]]['Nome']}")
            print(self.produtos[indices_maiores[0]])
