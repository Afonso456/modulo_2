escolha = "s"
while escolha== "s":
    op= input("Insira a operaçãoa realizar (+ ou s , - ou sub , / ou d , * ou m , somatorio) :")
    v1= float(input("Insira um nº:"))
    v2= float(input("Insira um nº:"))
    if op.lower() in "+s":
        resultado = v1 + v2 
    elif op.lower() in "-sub":
        resultado = v1 - v2 
    elif op.lower() in "/d":
        resultado = v1 / v2
    elif op.lower() in "*m":
        resultado = v1 * v2
    elif op.lower() in "somatorio":
        i1 = int(v1)
        i2 = int(v2)
        for i in range ( i1, i2 ):
            resultado = 0
            resultado = resultado + i
    else:
        print("Operação invalida")
        #definir o resultado com nada
        resultado = None
    if resultado is not None:
        print(resultado) 
    escolha= input("Pretende continuar a fazer contas:")
    escolha = escolha.strip().lower()