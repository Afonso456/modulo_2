#restaurante com 10 mesas e 50 lugares
mesas= 10 
lugares= mesas *5

for mesas_ocupadas in range (mesas):
    clientes=int(input("Insira o numero de clientes a entrar:"))
    if clientes > lugares:
        print("Não tem lugares disponiveis")
        break
    mesas= mesas - 1
    lugares = lugares - clientes
    print("Mesas ocupadas", mesas_ocupadas + 1)
    print("Lugares disponiveis", lugares)