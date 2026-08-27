class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def tamanho(self):
        if self.paginas <= 100:
            print('Curto')
        elif self.paginas > 100:
            print('Longo')
            
livro1 = Livro('livro1', 'murilo', 500)
livro2 = Livro('livro2', 'pedro', 2)

print('Livro1')
livro1.tamanho()

print('Livro2')
livro2.tamanho()