#programa que pede 2 numeros ao utilizador e as respctivas contas
operacoes=input("Insira a operação matematica que pretende fazer:")
v1= int(input("Insira o primeiro valor:"))
v2= int(input("Insira o segundo valor:"))

if operacoes == "soma":
    soma= v1 + v2
    print(f"A soma é {soma}")
if operacoes == "subtração":
    subtração= v1 - v2
    print(f"A subtração é {subtração}")
if operacoes == "divisão":
    div= v1 / v2
    print(f"A divisão é {div}")
if operacoes == "multiplicação":
    resto = v1 * v2
    print(f"O resto é {resto}")