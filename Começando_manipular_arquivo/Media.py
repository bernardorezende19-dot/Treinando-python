class Aluno:
    def __init__(self, nome:str, idade:int, nota:float) :
        self.nome = nome
        self.idade = idade
        self.nota = nota
    def calcular_media(self):
        return sum(self.nota) / len(self.nota)
if __name__ == "__main__":
    aluno1 = Aluno  ("Bernardo", 21,[6.1,8.5])
    aluno2 = Aluno  ("Lukas",19,[1.7,6.7])
    lista_alunos = [aluno1,aluno2]
    for aluno in lista_alunos:
        print(f"Nome: {aluno.nome} Média: {aluno.calcular_media():.2f}")
    