class Noduplo:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None
        
        
def menu():
    print('1 - Inserir jogador')
    print('2 - Listar')
    print('3 - Listar na ordem inversa')
    print('4 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao
        
def adicionar_inicio(lista, nome):
    novo = Noduplo(nome)
    
    
    if lista is None:
        lista = novo
        return lista
    
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista

def percorrer_frente(lista):
    aux = lista
    
    while aux != None:
        print('Nome - ', aux.nome)
        aux = aux.proximo
    
def percorrer_tras(lista):
    aux = lista
    while aux.proximo != None:
        aux = aux.proximo
        
    while aux != None:
        print('Nome - ', aux.nome)
        aux = aux.anterior
        
    
def main():
    lista = None
    opcao = None
    
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            nome = input('Digite um nome: ')
            lista = adicionar_inicio(lista, nome)
        elif opcao == 2:
            percorrer_frente(lista)
        elif opcao == 3:
            percorrer_tras(lista)
            
main()