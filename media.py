soma = 0
contar = 0
for i in range (3):
    n1=int (input("insira um numero:"))
    if n1 >= 20 and n1 <= 50:
        soma = soma + n1
        contar = contar +1
        media = soma // contar
print(media)