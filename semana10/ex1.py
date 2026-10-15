
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_cabeca(self, dado):
        novo = No(dado)

        if self.head == None:
            self.head = self.tail = novo
            return

        novo.proximo = self.head
        self.head.anterior = novo
        self.head = novo

    def inserircauda(self, dado):
        novo = No(dado)

        if self.tail == None:
            self.tail = self.head = novo
            return

        novo.anterior = self.tail
        self.tail.proximo = novo
        self.tail = novo

    def remover_cabeca(self):
        if self.head == None:
            print('Fila vazia')
            return

        dado = self.head.dado
        self.head = self.head.proximo

        if self.head == None:
            self.tail = None
        else:
            self.head.anterior = None

        print('Chamado atendido:', dado)

    def removercauda(self):
        if self.tail == None:
            print('Fila vazia')
            return

        dado = self.tail.dado
        self.tail = self.tail.anterior

        if self.tail == None:
            self.head = None
        else:
            self.tail.proximo = None

        print('Chamado atendido:', dado)

    def mostrarcabeca(self):
        if self.head == None:
            print('Fila vazia')
            return

        aux = self.head
        while aux != None:
            print('- ', aux.dado)
            aux = aux.proximo

def menu():
    print('1 - Adicionar chamado no fim da fila')
    print('2 - Adicionar chamado urgente no início da fila')
    print('3 - Atender chamado do início da fila')
    print('4 - Atender chamado do fim da fila')
    print('5 - Listar todos os chamados')
    print('6 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao

def main():
    opcao = 0
    deque = Deque()

    while opcao != 6:
        opcao = menu()

        if opcao == 1:
            dado = input('Descrição do chamado: ')
            deque.inserircauda(dado)

        elif opcao == 2:
            dado = input('Descrição do chamado urgente: ')
            deque.inserir_cabeca(dado)

        elif opcao == 3:
            deque.remover_cabeca()

        elif opcao == 4:
            deque.removercauda()

        elif opcao == 5:
            deque.mostrarcabeca()

        elif opcao == 6:
            print('Saindo do sistema')

        else:
            print('Opção inválida')

main()
