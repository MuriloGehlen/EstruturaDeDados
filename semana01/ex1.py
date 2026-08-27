class Produto:
    def __init__(self, preco, quantidade,):
        self.preco = preco
        self.quantidade = quantidade
        self.total = 0
    
    def calcular_total(self):
        self.total = self.preco * self.quantidade
    
    def mostrar_total(self):
        print(self.total)
    
arroz = Produto(10, 100)
arroz.calcular_total()
arroz.mostrar_total()

        