pos_maior = 1
maior= int (input("Nº"))
for i in range (9):
    n= int (input("Insira o primeiro valor:"))
    if n > maior:
        maior = n
        pos_maior= i +1

print("O maior é", maior, "e foi o",pos_maior,"a ser inserido ")