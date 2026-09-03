class Turma:
    def __init__(self, matricula, nome, nota, situacao):
        self.situacao = situacao
        self.matricula = matricula
        self.nome = nome
        self.nota = nota
        self.proximo = None
        
def menu():
    print('1 - Cadastrar novo aluno')
    print('2 - Listar todos os alunos cadastrados')
    print('3 - Listar alunos ativos no sistema')
    print('4 - Listar alunos desativados do sistema')
    print('5 - Buscar aluno')
    print('6 - Alterar nota final')
    print('7 - Alterar situação do aluno')
    print('8 - Remover um aluno')
    print('9 - Quantidade de alunos cadastrados')
    print('10 - Média das notas da turma')
    print('11 - Média das notas dos alunos ativos')
    print('12 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao


def inserir( lista, matricula, nome, nota, situacao): 
    novo = Turma(matricula, nome, nota, situacao)
    aux = lista
    
    
    if lista is None:
        lista = novo
        return lista
    
    while aux.proximo != None:
        aux = aux.proximo
        
    aux.proximo = novo
    return lista


def listar(lista): 
    aux = lista
    
    
    while aux != None:
        
        if aux.situacao == True:
            situacao = 'Ativado'
        else:
            situacao = 'Desativado'
            
        print('------------')
        print('Matricula - ',aux.matricula)
        print('Nome - ', aux.nome)
        print('Nota final - ', aux.nota)
        print('Situação - ' , situacao)
        print('------------')
        
        aux = aux.proximo    



def ativados(lista): 
    aux = lista

    while aux != None:
        if aux.situacao == True:
            print('------------')
            print('Matricula - ',aux.matricula)
            print('Nome - ', aux.nome)
            print('Nota final - ', aux.nota)
            print('------------')
        
        
        aux = aux.proximo


def desativados(lista):
    aux = lista

    while aux != None:
        if aux.situacao == False:
            print('------------')
            print('Matricula - ',aux.matricula)
            print('Nome - ', aux.nome)
            print('Nota final - ', aux.nota)
            print('------------')
        
        
        aux = aux.proximo



def buscar(lista):
    aux = lista
    matricula = int(input('Insira o número da matricula: '))
    
    while aux != None:
        if aux.matricula == matricula:
            print('Esse aluno está matriculado')
            print('Situação: ',aux.situacao)
        elif aux.proximo == None and aux.matricula != matricula:
            print('Aluno não encontrado')
        aux = aux.proximo
        
        
def notafinal(lista):
    aux = lista
    nome = None
    matricula = None
    
    print('1 - Buscar por matricula')
    print('2 - Buscar por nome')
    opcao = int(input('Digite a opção: '))
    
    if opcao == 1:
        matricula = int(input('Digite o numero da matricula: '))
    elif opcao == 2:
        nome = input('Digite o nome do aluno: ')
    
    
    while aux != None:
        if matricula != None:
            if aux.matricula == matricula:
                aux.nota = float(input('Digite a nova nota final: '))
                return lista
        elif nome != None:
            if aux.nome.lower() == nome:
                aux.nota = float(input('Digite a nova nota final: '))
                return lista
                
        aux = aux.proximo
        
def alterar(lista):
    aux = lista
    nome = None
    matricula = None
    
    print('1 - Buscar por matricula')
    print('2 - Buscar por nome')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        matricula = int(input('Digite o numero da matricula: '))
    elif opcao == 2:
        nome = input('Digite o nome do aluno: ')
    
    while aux != None:
        if matricula != None:
            if aux.matricula == matricula:
                aux.situacao = not aux.situacao
                return lista
        elif nome != None:
            if aux.nome.lower() == nome:
                aux.situacao = not aux.situacao
                return lista
        aux = aux.proximo


def remover(lista):
    aux = lista
    nome = None
    matricula = None

    if lista is None:
        print('Lista vazia')
        return lista

    print('1 - Buscar por matricula')
    print('2 - Buscar por nome')
    opcao = int(input('Digite a opção: '))

    if opcao == 1:
        matricula = int(input('Digite o numero da matricula: '))

    elif opcao == 2:
        nome = input('Digite o nome do aluno: ')

    
    if matricula != None:
        if lista.matricula == matricula:
            lista = lista.proximo
            return lista

    elif nome != None:
        if lista.nome.lower() == nome.lower():
            lista = lista.proximo
            return lista


    while aux.proximo != None:

        if matricula != None:
            if aux.proximo.matricula == matricula:
                aux.proximo = aux.proximo.proximo
                return lista

        elif nome != None:
            if aux.proximo.nome.lower() == nome.lower():
                aux.proximo = aux.proximo.proximo
                return lista

        aux = aux.proximo

    print('Aluno não encontrado')
    return lista
    
def quantidade(lista):
    aux = lista
    qtd = 0
    
    while aux != None:
        qtd += 1
        aux = aux.proximo
    print('Existem',qtd,'Alunos cadastrados')
    
def media(lista):
    aux = lista
    soma = 0
    qtd = 0
    
    while aux != None:
        soma += aux.nota
        qtd += 1
        aux = aux.proximo
    
    media = soma / qtd
    print('A media total das notas é de ',media)
    
    
def mediaativos(lista):
    aux = lista
    soma = 0
    qtd = 0
    
    while aux != None:
        if aux.situacao == True:
            soma += aux.nota
            qtd +=1
        aux = aux.proximo
        
    media = soma / qtd
    print('A média das notas dos alunos ativos é de: ',media)
    
def main():
    lista = None
    opcao = 0
    
    
    while opcao != 12:
        opcao = menu()
        if opcao == 1:
            matricula = int(input('Digite a matricula do estudante: '))
            nome = input('Digite o nome do estudante: ')
            nota = float(input('Digite a nota final do estudante: '))
            situacao = True
            lista = inserir(lista, matricula, nome, nota, situacao)
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            ativados(lista)
        elif opcao == 4:
            desativados(lista)
        elif opcao == 5:
            buscar(lista)
        elif opcao == 6:
            lista = notafinal(lista)
        elif opcao == 7:
            lista = alterar(lista)
        elif opcao == 8:
            lista = remover(lista)
        elif opcao == 9:
            quantidade(lista)
        elif opcao == 10:
            media(lista)
        elif opcao == 11:
            mediaativos(lista)

main()