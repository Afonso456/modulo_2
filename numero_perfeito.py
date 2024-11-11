#Programa que pede um numero e indica se ele é perfeito ou não
soma= 0
numero= int(input("Insira um numero:"))
for i in range(1,numero):
    resto= numero % i
    if resto == 0:
        soma = soma + i
if soma == numero:
    print("O numero é perfeito")
else:
    print("O numero não é perfeito")