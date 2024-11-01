#Programa que le a idade de um apessoa e indica a categoria onde se encontra
idade= int(input("Insira a suas idade:"))
if idade <10:
    print("Está na class infantil")
elif idade >= 10 and idade < 14:
    print("Está na classe os iniciados")
elif idade >= 14 and idade < 18:
    print("Está na classe dos juniores")
elif idade >= 18:
    print("Está na classe dos seniores")