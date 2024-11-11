numero= int(input("Introduza o limite maximo:"))
for k in range (1, numero):
    soma= 0
    for i in range(1,k):
        resto= k % i
        if resto == 0:
            soma = soma + i
    if soma == k:
        print(f"O numero {k} é perfeito")