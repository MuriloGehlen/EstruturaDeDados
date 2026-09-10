class Rodizio:
    def __init__(self, cliente, pizza):
        self.cliente = cliente
        self.pizza = pizza
        self.proximo = None
        self.anterior = None


def menu():
    print('1 - Adicionar cliente')
    print('2 - Remover cliente')
    print('3 - Simular rodizio')
    print('4 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao


def inserir(lista, cliente, pizza):
    novo = Rodizio(cliente, pizza)
    
    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista
    
    novo.proximo = lista
    novo.anterior = lista.anterior
    lista.anterior.proximo = novo
    lista.anterior = novo
    lista = novo
    return lista    
    
def remover(lista,dado):
    aux = lista
    
    if lista is None:
        print('Rodizio vazio')
        return
    
    while True:
        if dado.lower() == aux.cliente.lower():
            if aux.proximo == aux:
                lista = None
                return lista
            
            elif aux == lista:
                lista.anterior.proximo = lista.proximo
                lista.proximo.anterior = lista.anterior
                lista = lista.proximo
                return lista
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista

        elif aux.proximo == lista:
            return lista
        aux = aux.proximo
        
def simular(lista):
    aux = lista
    
    qtd = int(input('Digite quantas vezes deseja simular: '))
    
    for i in range(1,qtd +1):
        print(i, 'Simulação')

        aux.pizza = 'Com pizza'
        
        
        rodizio = lista
        while True:
            
            print('--------')
            print('Cliente - ',rodizio.cliente)
            print('Pizza - ',rodizio.pizza)
            print('--------')
            
            if rodizio.proximo == lista:
                break
            rodizio = rodizio.proximo
            
        aux.pizza = 'Sem pizza'
        aux = aux.proximo



def main():
    lista = None
    opcao = 0
    
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            cliente = input('Adicione um cliente: ')
            pizza = 'Sem pizza'
            lista = inserir(lista, cliente, pizza)
        elif opcao == 2:
            dado = input('Insira o nome da cliente para remover: ')
            lista = remover(lista,dado)
        elif opcao ==3:
            simular(lista)
            
main()