class Pilha:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        
        
def menu():
    print('1 - Empilhar dados')
    print('2 - Desempilhar dado do topo')
    print('3 - Listar pilha')
    print('4 - Mostrar dado no topo da pilha')
    print('5 - Verificar se a pilha esá vazia')
    print('6 - Mostrar tamanho da pilha')
    print('7 - Mostrar média de valores da pilha')
    print('8 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao    
    
        
def empilhar(pilha, dado):
    novo = Pilha(dado)
    
    
    if pilha is None:
        pilha = novo
        return pilha
    
    novo.proximo = pilha
    pilha = novo
    return pilha

def desempilhar(pilha):
    if pilha is None:
        print('Pilha vazia')
        return pilha
    
    pilha = pilha.proximo
    return pilha

def listar(pilha):
    aux = pilha
    
    if pilha is None:
        print('Pilha vazia')
        return pilha
    
    while aux != None:
        print('Dado - ',aux.dado)
        aux = aux.proximo
        
        
        
def topo(pilha):
    print(pilha.dado)
    
    
    
def esta_vazia(pilha):
    
    if pilha is None:
        print('Pilha vazia')
    else:
        print('Pilha não está vazia')
        
        
        
def tamanho(pilha):
    aux = pilha
    qtd = 0
    
    if pilha is None:
        print('Pilha vazia')
        return pilha
        
    while aux != None:
        qtd += 1
        aux = aux.proximo
    print('Existem ',qtd,'Dados na pilha')
    
    
def media(pilha):
    aux = pilha
    qtd = 0
    valor = 0
    
    if pilha is None:
        print('Pilha vazia')
        return pilha
    
    while aux != None:
        qtd += 1
        valor += aux.dado
        aux = aux.proximo
        
    valormedia = valor / qtd
    
    print('A média é de: ', valormedia)
    
def main():
    pilha = None
    opcao = None
    
    while opcao != 8:
        opcao = menu()
        if opcao == 1:
            dado = int(input('Digite um dado: '))
            pilha = empilhar(pilha,dado)
        elif opcao == 2:
            pilha = desempilhar(pilha)
        elif opcao == 3:
            listar(pilha)
        elif opcao == 4:
            topo(pilha)
        elif opcao == 5:
            esta_vazia(pilha)
        elif opcao == 6:
            tamanho(pilha)
        elif opcao == 7:
            media(pilha)
main()