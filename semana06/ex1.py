class Suporte:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None
        
def menu():
    print('1 - Inserir chamado')
    print('2 - Listar chamados na fila')
    print('3 - Remover chamado')
    print('4 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao        
        
def inserir(filafim, filainicio,nome):
    novo = Suporte(nome)
    
    if filainicio == None:
        filainicio = novo
        filafim = novo
        return filafim,filainicio
    
    
    filafim.proximo = novo
    novo.anterior = filafim
    filafim = novo
    return filafim, filainicio

def listar(filainicio):
    aux = filainicio
    qtd = 0
    
    while aux != None:
        if aux == filainicio:
            print('Proximo a ser chamado - ', aux.nome)
        else:
            print('Nome - ', aux.nome)
        print()
        qtd +=1
        aux = aux.proximo
    print('Faltam ',qtd,'para serem atendidos')
        
def remover(filainicio, filafim):
    
    if filainicio is None:
        print('Fila vazia')
        return None, None
    
    
    elif filainicio == filafim:
        print('Unico chamado na fila')
        return None, None
    
    filainicio = filainicio.proximo
    filainicio.anterior = None
    return filainicio, filafim


def main():
    filainicio = None
    filafim = None
    opcao = None

    while opcao !=4:
        opcao = menu()
        if opcao == 1:
            nome = input('Digite o nome de quem for o chamado: ')
            filafim, filainicio = inserir(filafim, filainicio, nome)
        elif opcao == 2:
            listar(filainicio)
        elif opcao == 3:
            filafim, filainicio = remover(filainicio, filafim)
            
main()