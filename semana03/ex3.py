class Playlist:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None
        
    
def menu(lista):
    print('1 - Adicionar músicas na playlist')
    print('2 - Listar todas as musicas')
    print('3 - Remover música')
    print('4 - Buscar música por nome ou artista')
    print('5 - Mostrar a duração total da playlist')
    print('6 - Avançar ou voltar a música')
    print('7 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao


def inserir(lista, id, nome, artista, duracao):
    novo = Playlist(id, nome, artista, duracao)

    if lista is None:
        lista = novo
        return lista
    
    novo.proximo = lista
    lista.anterior = novo
    lista = lista.anterior
    return lista

def listar(lista):
    aux = lista
    
    while aux != None:
        print('----------------')
        print('ID - ', aux.id)
        print('Nome - ', aux.nome)
        print('Artista - ', aux.artista)
        print('Duração - ', aux.duracao)
        print('----------------')
        aux = aux.proximo

    

def remover(lista, dado):
    aux = lista
    
    if lista is None:
        print('Lista vazia')
        return
    
    while aux != None:
        if aux.nome.lower() == dado.lower():
            if aux.proximo == aux.anterior == None: #unico
                lista = None
                return lista
            
            if aux == lista: #cabeça
                lista = lista.proximo
                lista.anterior = None
                return lista
        

            if aux.proximo == None: # fim
                aux = aux.anterior
                aux.proximo = None
                return lista
            
            #meio
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            return lista
            
                
        
        aux = aux.proximo

def buscar(lista):
        aux = lista
        qtd = 0
        print('1 - Buscar por nome')
        print('2 - Buscar por artista')
        opcao = int(input('Digite a opção: '))
        
        
        if opcao == 1:
            nome = input('Digite o nome da música: ')
        elif opcao == 2:
            artista = input('Digite o nome do artista: ')
            
        while opcao != None:
            if opcao == 1:
                if aux.nome.lower() == nome.lower():
                    print('Essa música existe na playlist')
                    return
                elif aux.proximo == None:
                    print('Essa música não existe na playlist')
                    return    
                
            elif opcao == 2:
                if aux.artista.lower() == artista.lower():
                    qtd += 1
                if aux.proximo == None and qtd > 0:
                    print('Existem', qtd, 'Musicas desse artista nessa playlist')
                    return
                elif aux.proximo == None and qtd == 0:
                    print('Não há musicas desse artista na playlist')
                    return
            
            aux = aux.proximo
    
    
def duracaototal(lista):
    aux = lista
    tempo = 0
    
    if lista is None:
            print('Lista Vazia')
            return
        
    while aux != None:
        tempo += aux.duracao
        aux = aux.proximo    
        
    print('O tempo total da plalylist é de: ',tempo)
    
    
def mudarmusica(lista):
    aux = lista
    opcao = 0
    
    while opcao != 4:
        print('1 - Mostrar música atual')
        print('2 - Avançar a música')
        print('3 - Retroceder a música')
        print('4 - Voltar')
        opcao = int(input('Digite a opção: '))
        
        if opcao == 1:
            print('Tocando agora: ')
            print(aux.nome,' de ',aux.artista)
        
        elif opcao == 2:
            if aux.proximo == None:
                aux = lista
            else:
                aux = aux.proximo
                
        elif opcao == 3:
            if aux.anterior == None:
                while aux.proximo != None:
                    aux = aux.proximo
            else:
                aux = aux.anterior    
                
    
def main():
    lista = None
    opcao = None
        
    while opcao != 7:
        opcao = menu(lista)
        if opcao == 1:
            id = input('Digite o ID da musica: ')
            nome = input('Digite o nome da musica: ')
            artista = input('Digite o nome do artista: ')
            duracao = float(input('Digite a duração da musica em minutos: '))
            lista = inserir(lista, id, nome, artista, duracao)
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            dado = input('Digite o nome da musica para remover: ')
            lista = remover(lista, dado)
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            duracaototal(lista)
        elif opcao == 6:
            mudarmusica(lista)
        
        
        
main()