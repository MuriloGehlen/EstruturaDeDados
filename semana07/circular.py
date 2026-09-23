class Noduplocircular:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None
        
        
def menu():
    print('1 - Adicionar no inicio')
    print('2 - Adicionar no fim')
    print('3 - Listar na ordem')
    print('4 - Listar na ordem inversa')
    print('5 - Remover dado')
    print('6 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao
        
def adicionar_inicio(lista, dado):
    novo = Noduplocircular(dado)
    
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


def adicionar_final(lista, dado):
    aux = lista
    novo = Noduplocircular(dado)
    
    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista
    
    novo.proximo = lista
    novo.anterior = lista.anterior
    lista.anterior.proximo = novo
    lista.anterior = novo
    return lista
        
    
    

def percorrer_frente(lista):
    aux = lista
    
    if lista is None:
        print('Lista vazia')
        return
    
    while True:
        print('Dado - ',aux.dado)
        if aux.proximo == lista:
            break
        aux = aux.proximo
        
def percorrer_tras(lista):
    aux = lista

    if lista is None:
        print('Lista vazia')
        return
    
    while True:
        aux = aux.anterior
        print('Dado - ',aux.dado)
        if aux == lista:
            break
        
def remover(lista, dado):
    aux = lista
    
    if lista is None:
        print('Lista vazia')
        return
    
    
    while True:
        if aux.dado == dado:
            if aux.proximo == aux:
                lista = None
                return lista
            
            elif aux == lista:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                lista = aux.proximo
                return lista
            
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista    
        if aux.proximo == lista:
            print('Dado não encontrado')
            return lista
        aux = aux.proximo
    
    
    
def main():
    lista = None
    opcao = None
    
    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            dado = int(input('Digite um dado: '))
            lista = adicionar_inicio(lista, dado)
        elif opcao == 2:
            dado = int(input('Digite um dado: '))
            lista = adicionar_final(lista, dado)
        elif opcao == 3:
            percorrer_frente(lista)
        elif opcao == 4:
            percorrer_tras(lista)
        elif opcao == 5:
            dado = int(input('Digite um dado para remover: '))
            lista = remover(lista, dado)
            
            
main()