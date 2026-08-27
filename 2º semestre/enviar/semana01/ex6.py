class Aluno:
    def __init__(self, nome, lista):
        self.nome = nome
        self.lista = lista
        self.media = 0
    def calcular_media(self):
        for i in self.lista:
            self.media += i
        self.media = self.media / 3
        print(self.media)
        
    def verificar_aprovacao(self):
        if self.media >= 7:
            print('Aprovado')
        else:
            print('Reprovado')
            
            
murilo = Aluno('murilo', [8,10,9])
pedro = Aluno('pedro', [5,3,0])

murilo.calcular_media()
murilo.verificar_aprovacao()
print()
pedro.calcular_media()
pedro.verificar_aprovacao()