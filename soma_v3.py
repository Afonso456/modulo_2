x= int (input("Insisra o primeiro valor a somar:"))
y= int (input("Insisra o limite de valores a somar:"))

soma= 0

if x < y:
    for i in range ( x , y + 1 ):
        soma= soma + i
else:
    for i in range( y , x + 1):
        soma= soma + i
print(soma)