class No:
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None
        
        
        
def menu():
    print('1 - inserir novo aluno')
    print('2 - Listar alunos')
    print('3 - Remover Aluno')
    print('4 - Buscar Aluno')
    print('5 - Situação dos alunos')
    opcao = int(input('Digite a opção: '))
    return opcao
        
        
        
        
def inserir(lista, id, nome, nota):
    novo = No(id, nome, nota)
            
    if lista is None:
        lista = novo
        return lista
        
    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista
    
def listar(lista):
    aux = lista
        
    while aux != None:
        print('--------')
        print('ID: ', aux.id)
        print('Nome: ', aux.nome)
        print('Nota: ', aux. nota)
        print('--------')
        aux = aux.proximo
        
def remover(lista, dado):
    aux = lista
    
    
    if lista is None:
        print('Lista vazia')
        return
    
    while aux != None:
        if aux.id == dado:
            #só um elemento
            if aux.proximo == aux.anterior == None:
                lista = None
                return lista
            #cabeça
            elif aux == lista:
                lista = lista.proximo
                lista.anterior = None
                return lista
             
            #ultimo elemento
            elif aux.proximo == None:
                aux = aux.anterior
                aux.proximo = None
                return lista
            
            
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            return lista
        aux = aux.proximo


def buscar(lista, dado):
    aux = lista
    
    while aux != None:
        if aux.id == dado:
            print('Aluno encontrado')
            return
        if aux.proximo == None:
            print('Aluno não encontrado')
            return
        aux = aux.proximo
    
    
def situacao(lista):
    aux = lista
    situacao = None
    
    if lista == None:
        print('Lista vazia')
        return lista
    
    while aux != None:
        if aux.nota >= 7:
            situacao = 'Aprovado'
        elif aux.nota >= 4 and aux.nota <= 6.9:
            situacao = 'Exame'
        elif aux.nota < 4:
            situacao = 'Reprovado'
        print('ID: ', aux.id)    
        print('Nome: ', aux.nome) 
        print('Situação: ', situacao )
        aux = aux.proximo
    
def main():
    opcao = 0
    lista = None
        
    while opcao != 100:
        opcao = menu()
        if opcao == 1:
            id = int(input('Digite o ID do aluno: '))
            nome = input('Digite o nome do aluno: ')
            nota = float(input('Digite a nota do aluno: '))
            lista = inserir(lista, id, nome, nota)
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            dado = int(input('Digite o ID do aluno: '))
            lista = remover(lista, dado)
        elif opcao == 4:
            dado = int(input('Digite o ID do aluno: '))
            buscar(lista, dado)
        elif opcao == 5:
            situacao(lista)
            
        
main()