class Corrida:
    def __init__(self, id):
        self.id = id
        self.bastao = False
        self.proximo = None
        self.anterior = None



def menu():
        print('1 - Adicionar atleta')
        print('2 - Remover atelta')
        print('3 - Simular percurso')
        print('4 - Sair')
        opcao = int(input('Digite a opção: '))
        return opcao

def inserir(lista, id):
    novo = Corrida(id)
    
    
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


def remover(lista, dado):
    aux = lista
    
    if lista is None:
        print('Lista vazia')
        return lista
    
    while True:
        if aux.id == dado:
            if aux.proximo == aux:
                print('único elemento na lista')
                return None

            elif aux == lista:
                lista.proximo.anterior = lista.anterior
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista
            
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            return lista
        
        elif aux.proximo == lista:
            print('Dado não encontrado')
            return lista
        aux = aux.proximo



def percurso(lista):
    aux = lista
    atleta = lista
    
    qtd = int(input('Digite a quantidade de turnos que deseja simular: '))
    
    for i in range (1,qtd + 1):
        print('Turno - ', i)
        
        aux.bastao = True
        
        atleta = lista
        while True:
            
            print('----')
            print(atleta.id)
            print(atleta.bastao)
            print('----')

            
            if atleta.proximo == lista:
                break
            
            atleta = atleta.proximo
            
        aux.bastao = False
        
        aux = aux.proximo
    
    
def main():
    opcao = 0
    lista = None
    
    
    
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            id = input('Insira o ID do atleta: ')
            lista = inserir(lista, id)
        elif opcao == 2:
            dado = input('Digite a ID do atleta a ser removido: ')
            lista = remover(lista,dado)
        elif opcao == 3:
            percurso(lista)    

    
main()