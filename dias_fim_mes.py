dias= int(input("Insira o dia:")) 
mes= str(input("Insira o mes:"))
ano= int(input("Insira o ano:"))
dias_mes= 31
if mes == 4 or mes== 6 or mes== 9 or mes== 11:
    dias_mes = 30
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        dias_mes= 29
    else:
        dias_mes= 28

faltam= dias_mes -dias
print(f"Faltam {faltam} dias para acabar o mes")