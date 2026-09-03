class Clinica:
    def __init__(self, codigo, nome, idade, prioridade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None
        
def menu():
    print('1 - Cadastrar paciente')
    print('2 - Remover paciente')
    print('3 - Buscar paciente')
    print('4 - Atender mais urgente')
    print('5 - Listar pacientes do primeiro ao ultimo')
    print('6 - Listar pacientes pela prioridade')
    print('7 - Listar pacientes do ultimo para o primeiro')
    print('8 - Informar quantos pacientes aguardam atendimento')
    print('9 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao
    
    
def cadastro(lista, codigo, nome, idade, prioridade):
    novo = Clinica(codigo, nome, idade, prioridade)
    
    
    if lista is None:
        lista = novo
        return lista
    

    novo.proximo = lista
    lista.anterior = novo
    lista = novo    
    return lista
    
    
    
    
    
def remover(lista, dado):
    aux = lista
    
    if lista is None:
        print('Fila vazia')
        return
    
    while aux != None:
        if aux.nome.lower() == dado or aux.codigo.lower() == dado:
            
            if aux == lista:
                lista = lista.proximo
                return lista
            
            if aux.anterior == aux.proximo == None:
                lista = None
                return lista
            
            if aux.proximo == None:
                aux = aux.anterior
                aux.proximo = None
                return lista
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista
        aux = aux.proximo
        
    print('Cliente não encontrado')
    return
        
    
def localizar(lista,codigo):    
    aux = lista
    
    if lista is None:
        print('Fila vazia')
        return
    
    while aux != None:
        if codigo.lower() == aux.codigo.lower():
            print('Esse paciente está cadastrado')
            return
        aux = aux.proximo    
    print('Paciente não encontrado')
    
    
    
def atenderurgente(lista):
    # Acabei deixando essa função por ultimo por achar a mais dificil de fazer do jeito que eu queria
    # Fiz nos 45 do 2º tempo e não tive tempo de testar tudo
    # portanto não sei se ela funciona inteiramente
    # Ao invés de só remover o com menos urgencia, eu movi o mais urgente para o começo da fila, para ser atendido agora
    # Mas sem a necessidade de cadastrar o com menos urgencia de novo, já que ele precisa ser atendido de qualquer forma
    
    aux = lista
    urgente = lista
    
    if lista is None:
        print('Lista vazia')
        return 
    
    if aux.proximo == aux.anterior == None:
        print('Há somente um paciente na fila')
        return lista
    
    while aux.proximo != None:
        if aux.prioridade < urgente.prioridade:
            urgente = aux
        aux = aux.proximo
    
    aux = lista
    while aux != None:
        if urgente == aux:
            
            if aux.anterior == None:
                print('Paciente já irá ser atendido por primeiro')
                return lista
            
            if aux.proximo == None:
                urgente.anterior.proximo = None
                urgente.proximo = lista
                lista.anterior = urgente
                urgente.anterior = None
                lista = urgente
                print('Fila alterada')
                return lista
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            urgente.proximo = lista
            lista.anterior = urgente
            urgente.anterior = None
            lista = urgente
            print('Fila alterada')
            return lista
            
        aux = aux.proximo
    
    

def primeiroultimo(lista):
    aux = lista
    
    if lista is None:
        print('Fila vazia')
        return
    
    while aux != None:
        print('------------')
        print('Código - ',aux.codigo)
        print('Nome - ',aux.nome)
        print('Idade - ',aux.idade)
        if aux.prioridade == 1:
            print('Prioridade - Emergência')
        elif aux.prioridade == 2:
            print('Prioridade - Muito urgente')
        elif aux.prioridade == 3:
            print('Prioridade - urgente')
        elif aux.prioridade == 4:
            print('Prioridade - Pouco urgente')
        else:
            print('Prioridade - Não urgente')
        print('------------')
        
        aux = aux.proximo
        
        
def listarprioridade(lista,dado):
    aux = lista
    
    while aux != None:
        if aux.prioridade == dado:
            print('------------')
            print('Código - ',aux.codigo)
            print('Nome - ',aux.nome)
            print('Idade - ',aux.idade)
            if aux.prioridade == 1:
                print('Prioridade - Emergência')
            elif aux.prioridade == 2:
                print('Prioridade - Muito urgente')
            elif aux.prioridade == 3:
                print('Prioridade - urgente')
            elif aux.prioridade == 4:
                print('Prioridade - Pouco urgente')
            else:
                print('Prioridade - Não urgente')
            print('------------')
        aux = aux.proximo
    if aux.prioridade != dado:
        print('Não há esta prioridade na fila')
        
        
        
def ultimoprimeiro(lista):
    aux = lista
    
    while aux.proximo != None:
        aux = aux.proximo
        
    while aux != None:
        print('------------')
        print('Código - ',aux.codigo)
        print('Nome - ',aux.nome)
        print('Idade - ',aux.idade)
        if aux.prioridade == 1:
            print('Prioridade - Emergência')
        elif aux.prioridade == 2:
            print('Prioridade - Muito urgente')
        elif aux.prioridade == 3:
            print('Prioridade - urgente')
        elif aux.prioridade == 4:
            print('Prioridade - Pouco urgente')
        else:
            print('Prioridade - Não urgente')
        print('------------')
        aux = aux.anterior
        

def aguardando(lista):
    aux = lista
    qtd = 0
    
    while aux != None:
        qtd += 1
        aux = aux.proximo
    
    print('Há ',qtd,'pacientes aguardando atendimento')
    
def main():
    lista = None
    opcao = 0
    
    while opcao != 9:
        opcao = menu()
        if opcao == 1:
            codigo = input('Digite o código do paciente: ')
            nome = input('Digite o nome do paciente: ')
            idade = input('Digite a idade do paciente: ')
            prioridade = 0
            while prioridade < 1 or prioridade > 5:
                print('1 - Emergência')
                print('2 - Muito urgente')
                print('3 - Urgente')
                print('4 - Pouco urgente')
                print('5 - Não urgente')
                prioridade = int(input('Digite o numero referente a urgencia do paciente: '))
            
            lista = cadastro(lista, codigo, nome, idade, prioridade)
        elif opcao == 2:
            dado = input('Digite o código ou o nome do paciente: ')
            lista = remover(lista,dado)
        elif opcao == 3:
            codigo = input('Digite o código do paciente: ')
            localizar(lista,codigo)
        elif opcao == 4:
            lista = atenderurgente(lista)
        elif opcao == 5:
            primeiroultimo(lista)
        elif opcao == 6:
            dado = 0
            while dado < 1 or dado > 5:
                print('1 - Emergência')
                print('2 - Muito urgente')
                print('3 - Urgente')
                print('4 - Pouco urgente')
                print('5 - Não urgente')
                dado = int(input('Digite a prioridade a ser listada'))
            listarprioridade(lista,dado)
        elif opcao == 7:
            ultimoprimeiro(lista)
        elif opcao == 8:
            aguardando(lista)
            
main()