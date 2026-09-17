class Jogador:
    def __init__(self, jogador):
        self.jogador = jogador
        self.proximo = None
        self.anterior = None


def menu():
    print('1 - Adicionar jogador ao final da fila')
    print('2 - Simular 1 rodada')
    print('3 - Simular N rodadas')
    print('4 - Mostrar fila')
    print('5 - Mostrar próximo a jogar')
    print('6 - Limpar fila')
    print('7 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao


def inserir(filafim, filainicio, jogador):
    novo = Jogador(jogador)

    if filainicio == None:
        filainicio = novo
        filafim = novo
        return filafim, filainicio

    filafim.proximo = novo
    novo.anterior = filafim
    filafim = novo
    return filafim, filainicio


def listar(filainicio):
    aux = filainicio
    posicao = 1

    if filainicio == None:
        print('Fila vazia')
        return

    while aux != None:
        print(posicao, ' - ', aux.jogador)
        posicao += 1
        aux = aux.proximo


def rodada(filainicio, filafim):
    if filainicio == None:
        print('Fila vazia')
        return filainicio, filafim

    print('Jogador que vai jogar - ', filainicio.jogador)

    if filainicio == filafim:
        return filainicio, filafim

    aux = filainicio

    filainicio = filainicio.proximo
    filainicio.anterior = None

    aux.proximo = None
    aux.anterior = filafim

    filafim.proximo = aux
    filafim = aux

    return filainicio, filafim


def proximo(filainicio):
    if filainicio == None:
        print('Fila vazia')
        return

    print('Próximo a jogar - ', filainicio.jogador)


def limpar(filainicio, filafim):
    return None, None


def main():
    filainicio = None
    filafim = None
    opcao = None

    while opcao != 7:
        opcao = menu()

        if opcao == 1:
            jogador = input('Digite o nome do jogador: ')
            filafim, filainicio = inserir(filafim, filainicio, jogador)

        elif opcao == 2:
            filainicio, filafim = rodada(filainicio, filafim)

        elif opcao == 3:
            qtd = int(input('Digite a quantidade de rodadas: '))

            for i in range(1, qtd + 1):
                print('Rodada - ', i)
                filainicio, filafim = rodada(filainicio, filafim)
                listar(filainicio)

        elif opcao == 4:
            listar(filainicio)

        elif opcao == 5:
            proximo(filainicio)

        elif opcao == 6:
            filainicio, filafim = limpar(filainicio, filafim)
            print('Fila limpa')


main()