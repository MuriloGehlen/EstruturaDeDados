class Deploy:
    def __init__(self, nome, duracao, ambiente, ativo):
        self.nome = nome
        self.duracao = duracao
        self.ambiente = ambiente
        self.ativo = ativo
        self.proximo = None
        self.anterior = None

def adiciona(lista, nome, duracao, ambiente, ativo):
    novo = Deploy(nome, duracao, ambiente, ativo)
    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista
    novo.anterior = lista.anterior
    novo.proximo = lista
    lista.anterior.proximo = novo
    lista.anterior = novo
    lista = novo
    return lista

def tempo(lista)
    aux = lista
    qtd = 0
    while True:
        qtd += aux.duracao
        aux = aux.proximo
        if aux.proximo == lista:
            break
    print(qtd)

def listar(lista):
    aux = lista
    opcao = int(input())
    if opcao == "a":
        while True:
            if aux.ambiente == "teste":
                print(aux.ambiente)
                print(aux.nome)
                print(aux.duracao)
                print(aux.ativo)
                if aux.proximo == lista:
                    break
            aux = aux.proximo
        while True:
            if aux.ambiente == "homologação":
                print(aux.ambiente)
                print(aux.nome)
                print(aux.duracao)
                print(aux.ativo)
                if aux.proximo == lista:
                    break
            aux = aux.proximo
        while True:
            if aux.ambiente == "produção":
                print(aux.ambiente)
                print(aux.nome)
                print(aux.duracao)
                print(aux.ativo)
                if aux.proximo == lista:
                    break
            aux = aux.proximo
    elif opcao == "b":
        while aux != None:
            if aux.ativo == True:
                print(aux.nome)
                print(aux.duracao)
                print(aux.ambiente)
                print(aux.ativo)

def ativar(lista, nome):
    aux = lista
    while True:
        if aux.nome == nome:
            aux.ativo = True
            return lista
        if aux.proximo == lista:
            break

def desativar(lista, nome):
    aux = lista
    while True:
        if aux.nome == nome:
            aux.ativo == False
            return lista
        if aux.proximo == lista:
            break
        aux = aux.proximo

def excluir(lista, nome)
    aux = lista
    if lista is None:
        return
    if aux == lista:
        lista.anterior.proximo = lista.proximo
        lista.proximo.anterior = lista.anterior
        lista = lista.proximo
        return lista
    aux.anterior.proximo = aux.proximo
    aux.proximo.anterior = aux.anterior
    return lista

def menu():
    opcao = int(input())
    return opcao

def main():
    lista = None
    opcao = None
    while opcao != 7:
        opcao = menu()
        if opcao == 1:
            nome = input()
            duracao = int(input())
            ambiente = input()
            ativo = bool(input())
            lista = adiciona(lista, nome, duracao, ambiente, ativo)
        if opcao == 2:
            listar(lista)
        if opcao == 3
            tempo(lista)
        if opcao == 4:
            lista = ativar(lista, nome)
        if opcao == 5:
            lista = desativar(lista, nome)
        if opcao == 6:
            lista = excluir(lista, nome)

main()