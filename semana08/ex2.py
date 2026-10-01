class Servidor:
    def __init__(self, id, nome, status):
        self.id = id
        self.nome = nome
        self.status = status
        self.proximo = None
        self.anterior = None

def inserir(lista, id, nome, status):
    novo = Servidor(id, nome, status)
    if lista is None:
        lista = novo
        return lista
    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def remover(lista, dado)
    aux = lista
    if lista is None:
        return None
    while aux != None:
        if aux.id == dado:
            if aux == lista:
                lista.proximo.anterior = None
                lista = lista.proximo
                return lista
            if aux.proximo == None
                aux.anterior.proximo = None
                return lista
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista
        aux = aux.proximo
    return lista

def desligar(lista, dado)
    aux = lista
    if lista is None:
        return
    while aux != None:
        if aux.id == dado:
            aux.status = not aux.status
            return lista
        aux = aux.proximo
    return lista

def percorrer(lista):
    aux = lista
    if lista is None:
        return
    opcao = int(input())
    if opcao == 1:
        while aux != None:
            print(aux.id)
            print(aux.nome)
            print(aux.status)
            aux = aux.proximo
    elif opcao == 2:
        while aux.proximo != None:
            aux = aux.proximo
        while aux != None:
            print(aux.id)
            print(aux.nome)
            print(aux.status)
            aux = aux.anterior

def menu():
    opcao = int(input())
    return opcao

def main():
    lista = None
    opcao = None
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            id = int(input())
            nome = str(input())
            status = bool(input())
            lista = inserir(lista, id, nome, status)
        elif opcao == 2:
            dado = int(input())
            lista = remover(lista, dado)
        elif opcao == 3: 
            dado = int(input())
            lista = desligar(lista, dado)
        elif opcao == 4:
            percorrer(lista)

main()