n1= int (input("Insira um numero inteiro:"))
primo = True
for i in range (2, n1):
    if n1 % i == 0:
        primo = False
if primo == True:
    print("O nº",n1,"é primo")
else:
    print("O nº" ,n1,"não é primo")