carga= 0
carga_maxima= 1000
total= 0
while carga < carga_maxima:
    peso= int(input("Insira o peso de cada mala em kg:"))
    total= carga_maxima - peso
    print(total)