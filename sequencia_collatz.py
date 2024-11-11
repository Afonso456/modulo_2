n= int(input("Insira um numero:"))
cont= 0
while n != 1:
    div= n % 2
    if div == 0:
        n = n // 2 
    else:
        n = n * 3 + 1
    print(n ,end =",")