from collections import namedtuple, deque, Counter, defaultdict

Alunos = namedtuple ("Aluno",["Nome","Idade"])

A1 = Alunos("Bernas","21")
A2 = Alunos("Malu","17")
A3 = Alunos("Lukita","20")

Chamada = deque()
Chamada.append (A2)
Chamada.append (A1)
Chamada.append (A3)


Quantidade_de_alunos = Counter() 
Quantidade_de_alunos[A1.Nome] += 1
Quantidade_de_alunos[A2.Nome] += 1
Quantidade_de_alunos[A3.Nome] += 1


Alunos_por_sala = defaultdict(list)
Sala = {
    "Bernas": "Sala A",
    "Malu": "Sala B",
    "Lukita": "Sala A",
}

for aluno in Chamada:
    Alunos_por_sala[Sala[aluno.Nome]].append(aluno.Nome)

print(Chamada)
print(Quantidade_de_alunos)
print("\nAlunos por sala:")
print(Alunos_por_sala)



