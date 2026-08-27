class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        
    def mostrar(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        
murilo = Contato('murilo', 1, 'murilo@')
pedro = Contato ('pedro', 2, 'pedro@' )
luiz = Contato ('luiz', 3, 'luiz@')

agenda = []
agenda.append(murilo)
agenda.append(pedro)
agenda.append(luiz)

for i in agenda:
    print(i.nome, i.telefone, i.email)
    