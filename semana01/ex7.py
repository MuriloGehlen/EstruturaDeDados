class Aluno:
    def __init__(self, nome, lista):
        self.nome = nome
        self.lista = lista
        self.media = 0
    
    def mediana(self):
        for i in self.lista:
            self.media += i
        self.media = self.media / 3
        print(self.nome,self.media)
    


murilo = Aluno('murilo', [8,7,10])
pedro = Aluno('pedro', [7,8,9])
luiz = Aluno('luiz', [5,6,2])
    
murilo.mediana()
pedro.mediana()
luiz.mediana()