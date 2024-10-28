x= int (input("Insisra o primeiro valor a somar:"))
y= int (input("Insisra o limite de valores a somar:"))
soma=0
if x < y:
    incremento = 1
else:
    incremento = -1 
for i in range ( x , y + incremento, incremento ):
    soma= soma + i
print(soma)