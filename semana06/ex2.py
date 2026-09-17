class Operacao:
    def __init__(self, operacao):
        self.operacao = operacao
        self.proximo = None
        
def menu():
    print('1 - Inserir operação na pilha')
    print('2 - Retirar ultima operação')
    print('3 - Mostrar ultima operação')
    print('4 - Mostrar todas as operações pendentes')
    print('5 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao
    
            
def inserir(pilha, operacao):
    novo = Operacao(operacao)
    
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
        print('Operação - ',aux.operacao) 
        print('-------')
        aux = aux.proximo
        
def remover(pilha):
    if pilha is None:
        print('pilha vazia')
        return pilha
    
    pilha = pilha.proximo
    return pilha

def ultima(pilha):
    if pilha is None:
        print('Pilha vazia')
        return pilha
    
    print('Ultima operação - ',pilha.operacao)
    
    
    
def main():
    pilha = None
    opcao = None
    
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            operacao = input('Digite uma operação: ')
            pilha = inserir(pilha, operacao)
        elif opcao == 2:
            pilha = remover(pilha)
        elif opcao == 3:
            ultima(pilha)
        elif opcao == 4:
            listar(pilha)
main()