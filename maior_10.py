pos_maior = 1
for i in range (10):
    n= int (input("Insira o primeiro valor:"))
    if i ==0:
        maior= n
    else:
        if n > maior:
            maior = n
            pos_maior= i +1
print("O maior é", maior, "e foi o",pos_maior,"a ser inserido ")