def class Sprint:
#class Sprint    
    def __init__(self, nome, responsavel):
        self.nome = nome
        self.responsavel = responsavel
        self.proximo = None

def inserir(lista, nome, responsavel):
    novo = Sprint(nome, responsavel
    #novo = Sprint(nome, responsavel)
    if lista is None:
        lista = novo
        return lista
    novo.proximo = lista
    lista = novo
    return lista

def listar(lista):
    aux = lista
    if lista is None:
        print()
        return None
    while aux != None
        print(aux.nome)
        print(aux.responsavel)
        aux = aux.proximo

def remover(lista, nome):
    aux = lista
    anterior = None
    if lista is None:
        print()
        return None
    while aux != None
    #while aux != None:
        if aux.nome == dado:
            if aux == lista:
                lista = lista.proximo
                return
            else:
                anterior.proximo = aux.proximo
                return lista
        anterior = aux
        aux = aux.proximo
    return lista

def main():
    lista = None
    nome = "Planejamento do Produto"
    responsavel = "Ana"
    inserir(lista, nome, responsavel)
    nome = "Implementação do Backend"
    responsavel = "João"
    inserir(lista, nome, responsavel)
    nome = "Teste automatizado"
    responsavel = "Carlo"
    inserir(lista, nome, responsavel)
    listar(lista)
    dado = "Planejamento do Produto"
    remover(lista, dado)

main()