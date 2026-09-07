class Onibus:
    def __init__(self, parada, onibus):
        self.parada = parada
        self.onibus = onibus
        self.proximo = None
        self.anterior = None


def menu():
    print('1 - Adicionar parada')
    print('2 - Remover parada')
    print('3 - Simular percurso')
    print('4 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao


def inserir(lista, parada, onibus):
    novo = Onibus(parada, onibus)
    
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
        print('Lista vazia')
        return
    
    while True:
        if dado.lower() == aux.parada.lower():
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

        aux.onibus = 'Com ônibus'
        
        
        volta = lista
        while True:
            
            print('--------')
            print('Parada - ',volta.parada)
            print('Situação - ',volta.onibus)
            print('--------')
            
            if volta.proximo == lista:
                break
            volta = volta.proximo
            
        aux.onibus = 'Sem ônibus'
        aux = aux.proximo



def main():
    lista = None
    opcao = 0
    
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            parada = input('Adicione uma parada: ')
            onibus = 'Sem ônibus'
            lista = inserir(lista, parada, onibus)
        elif opcao == 2:
            dado = input('Insira o nome da parada para remover: ')
            lista = remover(lista,dado)
        elif opcao ==3:
            simular(lista)
            
main()