numero= int(input("Insiria um numero inteiro:"))
for divisor in range(numero, 0 ,- 1):
    if numero % divisor == 0:
        print(divisor) 