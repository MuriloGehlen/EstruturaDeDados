class Futebolistico:
    def __init__(self, nome, gols):
        self.nome = nome
        self.gols = gols
        self.proximo = None
        
def menu():
    print('1 - Adicionar jogador no inicio da fila')
    print('2 - Listar jogadores')    
    print('3 - Adicionar jogador no final da lista')
    print('4 - Calcular média de gols do time')
    print('5 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao
    
        
def adicionar_inico(lista, nome, gols):
    novo = Futebolistico(nome, gols)
    
    if lista is None:
        lista = novo
        return lista
    
    
    novo.proximo = lista
    lista = novo
    return lista
    
def adicionarfim(lista, nome, gols):
    aux = lista
    novo = Futebolistico(nome, gols)
    
    if lista is None:
        lista = novo
        return lista
    
    while aux.proximo != None:
        aux = aux.proximo
    aux.proximo = novo
    return lista
    
def percorrer(lista):
    aux = lista
    
    if lista is None:
        print('Lista vazia')
        return
    
    while aux != None:
        print('------')
        print('nome - ',aux.nome)
        print('Gols - ',aux.gols)
        print('------')
        aux = aux.proximo
        
def media(lista):
    aux = lista
    jogadores = 0
    qtd = 0
    
    if lista is None:
        print('Lista vazia')
        return 
    
    while aux != None:
        qtd += aux.gols
        jogadores += 1
        aux = aux.proximo
    mediagol = qtd / jogadores
    print('Media de gols por jogador: ',mediagol)
    
        
        
def main():
    lista = None
    opcao = None
    
    
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            nome = input('Digite nome do jogador: ')
            gols = int(input('Digite a quantidade de gols: '))
            lista = adicionar_inico(lista, nome, gols)
        elif opcao == 2:
            percorrer(lista)
        elif opcao == 3:
            nome = input('Digite o nome do jogador: ')
            gols = int(input('Digite a quantidade de gols: '))
            lista = adicionarfim(lista, nome, gols)
        elif opcao == 4:
            media(lista)
            
            
main()
            