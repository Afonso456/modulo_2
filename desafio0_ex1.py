#Ler dois numeros e indicar se são iguais ou diferentes e calcula a sua diferença se diferentes
n1= int(input("Insira o primeiro valor:"))
n2= int(input("Insira o segundo valor:"))
if n1 == n2:
    print("Iguais") 
else:
    print("Diferentes")
    diferenca= n1 - n2
    if diferenca < 0:
        diferenca = diferenca * (-1)
    print(diferenca) 