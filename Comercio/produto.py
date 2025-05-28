from Comercio.vendedor import Vendedor


class Produto(Vendedor):
    def __init__(self, name, price, marca):
        self._name = name
        self._price = price
        self._marca = marca

    def mostrar(self):
        return f'Nome do produto: {self._name} | Marca: {self._marca} | Preço: {self._price}'
    
    def extrair_dados(self):
        return {"nome_do_produto": self._name, "marca":self._marca, "price":self._price}
  