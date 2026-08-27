class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
        
    def mostrarinfo(self):
        print('Nome do produto: ',self.nome)
        print('Preço do produto: ', self.preco)
        print('Quantidade em estoque: ', self.estoque)
        
    def addestoque(self):
        adicionar = int(input('Digite o valor a ser adicionado: '))
        self.estoque += adicionar
    
    def vender(self):
        venda = float(input('Digite a quantidade vendida: '))
        if self.estoque >= venda:
            self.estoque -= venda
        elif self.estoque < venda:
            print('Não temos essa quantidade disponivel')
    
    def calcular(self):
        valortotal = self.preco * self.estoque
        print(valortotal)
    


nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
qtdestoque = float(input('Digite a quantidade em estoque: '))
loja1 = Produto(nome, preco, qtdestoque)



opcao = 0

while opcao != 5:
    print('1 - Exibir informações do produto')
    print('2 - Adicionar ao estoque')
    print('3 - Realizar venda')
    print('4 - Calcular o valor total no estoque')
    print('5 - Sair')
    opcao = int(input('Digite uma opcao: '))
    
    if opcao == 1:
        loja1.mostrarinfo()
    if opcao == 2:
        loja1.addestoque()
    if opcao == 3:
        loja1.vender()
    if opcao == 4:
        loja1.calcular()