class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcular_bonus(self):
        if self.cargo == 'gerente':
            self.salario = self.salario * 1.10
        else:
            self.salario = self.salario * 1.05
        print(self.salario)
    
murilo = Funcionario('murilo', 10000, 'gerente')
pedro = Funcionario('pedro', 5, 'lavadordelouca')

murilo.calcular_bonus()
pedro.calcular_bonus()