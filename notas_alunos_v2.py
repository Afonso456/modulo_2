soma= 0
positivas= 0
N_ALUNOS= 10
for i in range (1,11):
    notas =int(input("Insira a nota:"))
    soma= soma + notas
    if notas >= 10:
        positivas= positivas + 1
media = soma / N_ALUNOS
print(round(media,2))
print("Nº de positivas:",positivas / 10 * 100)
print("Nº de negativas:", N_ALUNOS - positivas / 100)