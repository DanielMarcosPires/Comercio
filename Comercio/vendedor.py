class Vendedor:
    def __init__(self, name:str, empresa:str):
        if type(name) == str and type(empresa) == str:
            self._name = name
            self._empresa = empresa
            self._produtos = []
        else:print("O tipo de um desses dados estão incorretos! Ambos os dados devem ser Strings")

    def mostrar_vendedor(self):
        return {"Nome": self._name, "Empresa": self._empresa}

    def adicionar_produto(self, produto):
        self._produtos.append(produto)
    
    def mostrar_produtos(self):
        print(f"\nProdutos do vendedor: {self._name}:")
        
        for produto in self._produtos:
            item:dict = produto
            print(f" Nome do produto: {item['nome_do_produto']} \n Marca: {item['marca']} \n Preço: {item['price']}")

        return self._produtos
    
    def preco_total(self):
        preco_total = 0
        for produto in self._produtos:
            item:dict = produto
            preco_total += item['price']
        #print(f"{self._name} Valor total de vendas: {preco_total}")
        return preco_total
    
    