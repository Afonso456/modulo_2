ano= int(input("Insira o ano em que se encontra:"))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano inserido é bissexto")
else:
    print("O ano inserido não é bisexto")
