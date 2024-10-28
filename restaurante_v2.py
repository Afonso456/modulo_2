mesas= 10 
lugares= mesas *5

while mesas > 0:
    clientes=int(input("Insira o numero de clientes a entrar:"))
    if clientes > lugares:
        print("Não tem lugares disponiveis")
        break
    mesas= mesas - 1
    lugares = lugares - clientes
    print("Mesas ocupadas", 10 - mesas)
    print("Lugares disponiveis", lugares)
print ("O restaurante esta cheio")