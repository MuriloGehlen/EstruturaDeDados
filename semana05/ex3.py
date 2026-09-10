import random

class Roleta:
    def __init__(self, guerreiros):
        self.guerreiros = guerreiros
        self.proximo = None
        self.anterior = None
        
def menu():
    print('1 - Inserir novo guerreiro')
    print('2 - Listar guerreiros')
    print('3 - Jogar Roleta')
    print('4 - Sair')
    opcao = int(input('Insira uma opção: '))
    return opcao


def inserir(lista, guerreiros, ):
    
    novo = Roleta(guerreiros, )
    
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


def listar(lista):
    aux = lista
    
    if lista is None:
        print('Não há guerreiros para jogar, tente convidar alguns')
        return lista
    
    while True:
        print('--------')
        print('Guerreiro - ', aux.guerreiros)
        print('--------')
        
        if aux.proximo == lista:
            break
            
        aux = aux.proximo


def jogar(lista):
    
    if lista is None:
        print('Não há guerreiros para jogar.')
        return lista
    
    qtd = 0
    aux = lista
    
    while True:
        qtd += 1
        
        if aux.proximo == lista:
            break  
        aux = aux.proximo
    
    while qtd > 1:
        sorteado = random.randint(1, qtd)
        aux = lista

        for i in range(1, sorteado):
            aux = aux.proximo
        
        print('Guerreiro eliminado - ', aux.guerreiros)
        
    
        if aux == lista:
            lista = aux.proximo
        

        aux.anterior.proximo = aux.proximo
        aux.proximo.anterior = aux.anterior
        
        qtd -= 1
    
    print('Sobrevivente - ', lista.guerreiros)
    
    return lista


def main():
    lista = None
    opcao = None
    
    while opcao != 4:
        opcao = menu()
        
        if opcao == 1:
            guerreiros = input('Digite o nome de um guerreiro: ')
            lista = inserir(lista, guerreiros, )
            
        elif opcao == 2:
            listar(lista)
            
        elif opcao == 3:
            lista = jogar(lista)
    
main()