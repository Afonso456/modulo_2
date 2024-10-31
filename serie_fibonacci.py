soma= 0
x1 = 0
x2= 1
n= int(input("Insira a quantidade de numero que pretende somar:"))
print(x1,"\n",x2)
for i in range(n -2):
    soma = x1 + x2
    x1 = x2 
    x2 = soma 
    print(soma)