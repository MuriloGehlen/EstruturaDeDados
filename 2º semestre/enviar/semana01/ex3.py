class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def atualizar_estoque(self, quantidade):
        self.estoque = self.estoque + quantidade
    
    def mostrar_valores(self):
        print('Produto: ',self.nome)
        print('Preço: ', self.preco)
        print('Quantidade em estoque: ' ,self.estoque)
        
arroz = Produto('arroz', 10, 20)
feijao = Produto('feijão', 15, 8)

arroz.mostrar_valores()
print()
feijao.mostrar_valores()
print()
print('Após mudanças: ')
print()
arroz.atualizar_estoque(10)
feijao.atualizar_estoque(30)
arroz.mostrar_valores()
print()
feijao.mostrar_valores()