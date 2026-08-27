class No:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador
        self.proximo = None
        self.anterior = None
        
def menu():
    print('1 - Inserir No')
    print('2 - Listar Nos')
    print('3 - Remover No')
    print('4 - Verificar se no existe')
    print('5 - sair')
    opcao = int(input('Digite a opção: '))
    return opcao

        
def inserir(lista, nome, identificador):
        novo = No(nome, identificador)
        
        if lista == None:
            lista = novo
            return lista
        
        novo.proximo = lista
        lista.anterior = novo
        lista = novo
        return lista
        
def listar(lista):
    aux = lista
    
    while aux != None:
        print('----------------')
        print('Nome: ', aux.nome)
        print('Identificador: ', aux.identificador)
        print('----------------')
        aux = aux.proximo
        
def remover(lista, id):
    aux = lista
    
    if lista is None:
        print('Lista Vazia')
        return
    
    while aux != None:
        if aux.identificador == id: #unico elemento na lista
            if aux.proximo == aux.anterior == None:
                lista = None
                return lista
            
            elif aux == lista:#cabeça da lista
                lista.proximo.anterior = None
                lista = lista.proximo
                return lista
            
            elif aux.proximo == None: #final da lista
                aux = aux.anterior
                aux.proximo = None
                return lista
            
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            return lista
        
        aux = aux.proximo
        
        
def buscar(lista):
    aux = lista
    opcao = None
    
    print('1 - Buscar por nome do no')
    print('2 - Buscar por identificador do no')
    opcao = int(input('digite a opção: '))
    
    if opcao == 1:
        dado = input('Digite o nome do no: ').lower()
    elif opcao == 2:
        dado = input('Digite o identificador do no: ').lower()
    if lista is None:
        print('Lista Vazia')
    
    while aux != None:   
        if aux.nome == dado or aux.identificador == dado:
            print('Esse no existe na lista')
            return
        else:
            print('No não encontrado')
            return
        
    aux = aux.proximo
        
        
def main():
    opcao = 0
    lista = None
    
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            nome = input('Digite o nome do No: ').lower()
            identificador = input('Digite o identificador: ').lower()
            lista = inserir(lista, nome, identificador)
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            id = input('Digite o identificador do No: ')
            lista = remover(lista, id)
        elif opcao == 4:
            buscar(lista)
    
main()    