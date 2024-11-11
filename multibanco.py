saldo=0
op= None
while op != "4" or saldo < 0:
    print("ATM\n1.Ver saldo\n2.Depositos\n3.Levantamentos\n4.Terminar")
    op= input()
    if op == "1" and saldo >= 0:
        print(f"O seu saldo é de {saldo} €")
    if op == "2":
        deposito = float(input("Insira o valor a depositar:"))
        if deposito != round(deposito, 2):
            print("O valor não é valido. So pode ter duas casas decimais")
            continue
        if deposito <= 0.01 and deposito > 10000:
            print("O valor introduzido não é valido")
        else:
            saldo = saldo + deposito
            print(f"O seu saldo atual é de {saldo} €")
    if op == "3" and saldo >= 0: 
        levantamento = float(input("Insira o valor a levantar:"))
        if levantamento != round(levantamento, 2):
            print("O valor inserido não é valido. So pode ter duas casas decimais")
        if levantamento < 10 or levantamento > 400 or levantamento > saldo:
            print("O valor inserido é invalido")
        else:
            saldo = saldo - levantamento 
            print(f"O seu saldo é de {saldo} €")
    if op == "4":
        break
