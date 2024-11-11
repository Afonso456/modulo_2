#Programa que lê o numero de alunos de uma turma e as suas notas e indica o numero do melhor aluno
melhor_nota= -1
melhor_aluno= 0
n_alunos= int(input("Insira o numerode alunos:"))
for i in range(n_alunos):
    nota= int(input(f"Nota do aluno nº {i+1}:"))
    if nota > melhor_nota:
        melhor_nota = nota
        melhor_aluno = i + 1
print(f"O aluno com melhor nota é o nº {melhor_aluno}")