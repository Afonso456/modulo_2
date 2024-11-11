#Programa que lê o peso de uma mala e indica se o peso maximo foi atingido
limite= 1000
cont= 0
while limite >= 0:
    peso= int(input("Insira o peso de cada mala em kg:"))
    if peso > limite:
        break
    cont = cont + 1
    limite= limite - peso
    print(f"Ainda pode transportar mais {limite} kg")
print(f"O valor a cobrar pelo transporte é de {cont * 20} €")