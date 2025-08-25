# Sistema de Escola

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        super().apresentar()

    def estudar(self):
        print(f'{self.nome} está estudando.')

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        print(f'{self.nome} está ensinando {self.disciplina}.')

a1 = Aluno("Caua", 17, "2024001")
p1 = Professor("João", 20, "Programação")

a1.estudar()
p1.ensinar()
