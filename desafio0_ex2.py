#Programa que lê a hora do dia e indica a parte do dia
hora= int(input("Insira o hora do dia:"))
if hora >= 5 and hora <= 7:
    print("Madrugada")
elif hora >= 8 and hora <= 12:
    print("Manhã")
elif hora >= 13 and hora<= 19:
    print("Tarde")
else:
    print("Noite")