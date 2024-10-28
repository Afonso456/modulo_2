soma= 0
N_ALUNNOS= 10
for i in range (1,11):
    notas =int(input("Insira a nota:"))
    soma= soma + notas
media = soma / N_ALUNNOS
print(round(media,2))