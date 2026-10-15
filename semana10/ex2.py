
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

        print('Cliente atendido:', dado)

    def mostrarcabeca(self):
        if self.head == None:
            print('Fila vazia')
            return

        aux = self.head
        while aux != None:
            print('- ', aux.dado)
            aux = aux.proximo

def menu():
    print('1 - Adicionar cliente comum')
    print('2 - Adicionar cliente preferencial')
    print('3 - Atender cliente')
    print('4 - Mostrar fila')
    print('5 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao

def main():
    opcao = 0
    deque = Deque()

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            dado = input('Nome do cliente comum: ')
            deque.inserircauda(dado)

        elif opcao == 2:
            dado = input('Nome do cliente preferencial: ')
            deque.inserir_cabeca(dado)

        elif opcao == 3:
            deque.remover_cabeca()

        elif opcao == 4:
            deque.mostrarcabeca()

        elif opcao == 5:
            print('Saindo do sistema')

        else:
            print('Opção inválida')

main()
