x= int (input("Insisra o primeiro valor a somar:"))
y= int (input("Insisra o limite de valores a somar:"))

if x > y:
    t = x
    x = y
    y = t
soma= 0
for i in range ( x , y + 1 ):
    soma= soma + i
print(soma)