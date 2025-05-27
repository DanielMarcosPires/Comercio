class Vendedor:
    def __init__(self, name:str, empresa:str):
        if type(name) == str and type(empresa) == str:
            self._name = name
            self._empresa = empresa
        else:print("O tipo de um desses dados estão incorretos! Ambos os dados devem ser Strings")

    def mostrar(self):
        return f'Nome do vendedor: {self._name} | Empresa: {self._empresa}'
    
    def extrair_dados(self):
        return {"nome": self._name, "empresa":self._empresa}