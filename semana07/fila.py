class Chatbot:
    def __init__(self, usuario, minutos):
        self.usuario = usuario
        self.minutos = minutos
        self.proximo = None
        self.anterior = None
        

def menu():
    print('1 - Adicionar cliente na fila')
    print('2 - Atender cliente da fila')
    print('3 - Listar clientes na fila')
    print('4 - Mostrar proximo a ser atendido')
    print('5 - Mostrar se há clientes na fila')
    print('6 - Mostrar quantidade de clientes')
    print('7 - Calcular média do tempo de espera')
    print('8 - Sair')        
    opcao = int(input('Digite uma opção: '))
    return opcao
        
def enfileirar(filainicio, filafim, usuario, minutos):
    novo = Chatbot(usuario, minutos)
    
    if filainicio is None:
        filainicio = novo
        filafim = novo
        return filainicio, filafim
    
    filafim.proximo = novo
    novo.anterior = filafim
    filafim = novo
    return filainicio, filafim

def desenfileirar(filainicio, filafim):
    aux = filainicio
    
    if filainicio is None:
        print('Fila vazia')
        return filainicio, filafim
    
    if filainicio == filafim:
        print('Ultimo cliente atendido')
        return None, None
    
    filainicio = filainicio.proximo
    filainicio.anterior = None
    return filainicio, filafim

def percorrer(filainicio):
    aux = filainicio
    
    while aux != None:
        print('Usuário - ',aux.usuario)
        print('Tempo de espera - ', aux.minutos)
        aux = aux.proximo

def frente(filainicio):
    print('Proximo a ser atendido: ',filainicio.usuario)

def esta_vazia(filainicio):
    if filainicio == None:
        print('Fila vazia')
    else:
        print('Usuários aguardando atendimento')

def tamanho(filainicio):
    aux = filainicio
    qtd = 0
    
    while aux != None:
        qtd += 1
        aux = aux.proximo
        
    print('Existem, ', qtd,'Clientes aguardando atendimento')

def mediatempo(filainicio):
    aux = filainicio
    qtd = 0
    tempo = 0
    
    while aux != None:
        qtd += 1
        tempo += aux.minutos
        aux = aux.proximo
    
    media = tempo / qtd    
        
    print('A média de tempo por cliente é de: ',media)
    
def main():
    filainicio = None
    filafim = None
    opcao = None
    
    while opcao != 8:
        opcao = menu()
        if opcao == 1:
            usuario = input('Digite o nome do usuário: ')
            minutos = int(input('Digite o tempo de espera em minutos: '))
            filainicio, filafim = enfileirar(filainicio, filafim, usuario, minutos)
        elif opcao == 2:
            filainicio, filafim = desenfileirar(filainicio, filafim)
        elif opcao == 3:
            percorrer(filainicio)
        elif opcao == 4:
            frente(filainicio)
        elif opcao == 5:
            esta_vazia(filainicio)
        elif opcao == 6:
            tamanho(filainicio)
        elif opcao == 7:
            mediatempo(filainicio)
            
main()