class Carrinho:

    def __init__(self, nome_produto, preco):
        self.nome_produto = nome_produto
        self.preco = preco


class Produto:

    def __init__(self):
        self.carrinho_produtos = []

    def inserir_produto(self, produto: Carrinho):
        self.carrinho_produtos.append(produto)

    def mostrar_lista(self):
        for produtos in self.carrinho_produtos:
            print(f"Produto: {produtos.nome_produto}, Preço: R${produtos.preco:.2f}")

compra_1 = Carrinho('Batata', 12.90)
compra_2 = Carrinho('Coca Cola', 8.99)
compra_3 = Carrinho('Requeijão', 6.99)


produto = Produto()
produto.inserir_produto(compra_1)
produto.inserir_produto(compra_2)
produto.inserir_produto(compra_3)
produto.mostrar_lista()

