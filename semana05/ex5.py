class Hospital:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None


def menu():
    print('1 - Inserir paciente')
    print('2 - Remover paciente')
    print('3 - Listar pacientes')
    print('4 - Simular atendimento')
    print('5 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao


def inserir(lista, nome, idade, prioridade):
    novo = Hospital(nome, idade, prioridade)
    
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


def remover(lista, dado):
    aux = lista
    
    if lista is None:
        print('Fila vazia')
        return lista
    
    while True:
        if dado.lower() == aux.nome.lower():
            if aux.proximo == aux:
                lista = None
                return lista
            
            elif aux == lista:
                lista.anterior.proximo = lista.proximo
                lista.proximo.anterior = lista.anterior
                lista = lista.proximo
                return lista
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista
        
        elif aux.proximo == lista:
            print('Paciente não encontrado')
            return lista
        
        aux = aux.proximo


def listar(lista):
    aux = lista
    
    if lista is None:
        print('Fila vazia')
        return lista
    
    while True:
        print('--------')
        print('Nome - ', aux.nome)
        print('Idade - ', aux.idade)
        
        if aux.prioridade == 1:
            print('Prioridade - Emergência')
        elif aux.prioridade == 2:
            print('Prioridade - Urgente')
        else:
            print('Prioridade - Normal')
            
        print('--------')
        
        if aux.proximo == lista:
            break
        
        aux = aux.proximo


def atender(lista):
    if lista is None:
        print('Fila vazia')
        return lista
    
    while lista != None:
        aux = lista
        atendimento = None
        
        while True:
            if aux.prioridade == 1:
                atendimento = aux
                break
            
            if aux.proximo == lista:
                break
            
            aux = aux.proximo
        
        if atendimento is None:
            aux = lista
            
            while True:
                if aux.prioridade == 2:
                    atendimento = aux
                    break
                
                if aux.proximo == lista:
                    break
                
                aux = aux.proximo
        
        if atendimento is None:
            aux = lista
            
            while True:
                if aux.prioridade == 3:
                    atendimento = aux
                    break
                
                if aux.proximo == lista:
                    break
                
                aux = aux.proximo
        
        if atendimento is None:
            break
        
        print('Paciente atendido - ', atendimento.nome)
        
        if atendimento.proximo == atendimento:
            lista = None
        elif atendimento == lista:
            lista.anterior.proximo = lista.proximo
            lista.proximo.anterior = lista.anterior
            lista = lista.proximo
        else:
            atendimento.anterior.proximo = atendimento.proximo
            atendimento.proximo.anterior = atendimento.anterior


def main():
    lista = None
    opcao = 0
    
    while opcao != 5:
        opcao = menu()
        
        if opcao == 1:
            nome = input('Digite o nome do paciente: ')
            idade = int(input('Digite a idade do paciente: '))
            prioridade = 0
            
            while prioridade < 1 or prioridade > 3:
                print('1 - Emergência')
                print('2 - Urgente')
                print('3 - Normal')
                
                prioridade = int(input('Digite o numero referente a urgencia do paciente: '))
            
            lista = inserir(lista, nome, idade, prioridade)
        
        elif opcao == 2:
            dado = input('Digite o nome do paciente a ser removido: ')
            lista = remover(lista, dado)
        
        elif opcao == 3:
            listar(lista)
        
        elif opcao == 4:
            lista = atender(lista)


main()