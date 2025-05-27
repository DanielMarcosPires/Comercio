from Comercio.produto import Produto
from Comercio.vendedor import Vendedor


produto = Produto("apple", 20, "Fazenda de alguém")
vendedor = Vendedor(
    name="Daniel",
    empresa="G&P"
)

dadosDoProduto = produto.extrair_dados()
dadosDoVendedor = vendedor.extrair_dados()

print(
    {
        "vendedor":dadosDoVendedor,
        "estoque":dadosDoProduto
    }
)