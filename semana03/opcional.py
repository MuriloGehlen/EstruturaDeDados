class Agenda:
    def __init__(self, tarefa, data):
        self.tarefa = tarefa
        self.data = data
        self.proximo = None
        self.anterior = None
        
        
def menu():
    print('1 - Inserir nova tarefa')
    print('2 - Remover tarefa')
    print('3 - Listar todas as tarefas')
    print('4 - Sair')
    opcao = int(input('Digite sua opção: '))        
    return opcao
        
        
def inserir(lista, tarefa, data):
    novo = Agenda(tarefa, data)
    
    if lista is None:
        lista = novo
        return lista
    
    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista


def horacerta():
    dia = 0
    mes = 0
    ano = 0
    
    print('Digite o dia, mês e ano dessa tarefa: ')
    
    while dia < 1 or dia > 31:
        dia = int(input('Dia: '))
        if dia < 1 or dia > 31:
            print('Dia inválido')
        
    while mes < 1 or mes > 12:
        mes = int(input('Mês: '))
        if mes < 1 or mes > 12:
            print('Mês inválido')
    
    ano = int(input('Ano: '))
    
    dia = str(dia)
    mes = str(mes)
    ano = str(ano)
    
    return dia,mes,ano



def remover(lista, dado):
    aux = lista
    
    if lista is None:
        print('Lista Vazia')
        return
    
    while aux != None:
        if aux.tarefa.lower() == dado.lower():
            if aux.proximo == aux.anterior == None:
                lista = None
                return lista
            
            elif aux.anterior == None:
                lista = lista.proximo
                lista.anterior == None
                return lista
            
            elif aux.proximo == None:
                aux = aux.anterior
                aux.proximo = None
                return lista
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista
        else:
            print('Dado não encontrado')
        
        aux = aux.proximo
    

def listar(lista):
    aux = lista
    
    if lista is None:
        print('Lista Vazia')
        return
    
    while aux != None:
        print('-----------')
        print('Tarefa - ',aux.tarefa)
        print('Data - ', aux.data)
        print('-----------')

        aux = aux.proximo
    
    
    
def main():
    opcao = None
    lista = None
    
    
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            tarefa = input('Digite a descrição da tarefa: ')
            dia,mes,ano = horacerta()
            data = dia + '/' + mes + '/' + ano
            lista = inserir(lista, tarefa, data)
        elif opcao == 2:
            dado = input('Digite a descrição da tarefa a ser removida: ')
            lista = remover(lista,dado)
        elif opcao == 3:
            listar(lista)
            
main()