escolha= "s"
soma= 0
while escolha == "s":
    lista= input("Insira a lista na qual pretende votar:")
    votos= int(input("Insira o numero de votos:"))
    total = votos
    soma1= total
    soma= soma + total
    print(soma)
    escolha= input("Deseja continuar:")
    if escolha == "n":
        break