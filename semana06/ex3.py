class Carro:
    def __init__(self, carro):
        self.carro = carro
        self.proximo = None


def inserir(pilha, carro):
    novo = Carro(carro)

    if pilha is None:
        pilha = novo
        return pilha

    novo.proximo = pilha
    pilha = novo
    return pilha


def listar(pilha):
    aux = pilha

    while aux != None:
        print('-------')
        print('Carro - ', aux.carro)
        print('-------')
        aux = aux.proximo


def remover(pilha):
    if pilha is None:
        print('Garagem vazia')
        return pilha

    pilha = pilha.proximo
    return pilha


def main():
    pilha = None

    for i in range(1, 21):
        carro = 'Carro ' + str(i)
        pilha = inserir(pilha, carro)

    print('Carros cadastrados:')
    listar(pilha)

    carro = input('Digite o carro que deseja retirar: ')

    aux = pilha
    encontrou = False

    while aux != None:
        if aux.carro.lower() == carro.lower():
            encontrou = True
            break
        aux = aux.proximo

    if encontrou == False:
        print('Carro não encontrado')
    else:
        print('Carros retirados:')

        while pilha.carro.lower() != carro.lower():
            print('Carro - ', pilha.carro)
            pilha = remover(pilha)

        print('Carro - ', pilha.carro)
        pilha = remover(pilha)


main()