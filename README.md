from dataclasses import dataclass
@dataclass
class Aluno:
    nome: str
    idade: int
    notas; list
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
        
if __name__ == "__main__":
    aluno1 = Aluno("Lukas", 19,[4.5, 6.9, 2.5])
    aluno2 = Aluno("Carlos",20,[3.5, 7.8, 0.5])
    aluno3 = Aluno("Matheus",35,[7.0, 3.5, 9.4])
    lista_alunos = [aluno1, aluno2, aluno3]
    for aluno in lista_alunos:
    print(f"Nome:{aluno.nome}, Média: {aluno.calcular_media():.2f}")
