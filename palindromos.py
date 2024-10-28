palavra= input("Insira uma palvra:")
len(palavra)
frase_invertida= ""
for i in range(len(palavra) -1,-1,-1):
    frase_invertida = frase_invertida + palavra[i]
if frase_invertida == palavra:
    print(f"É palavra {palavra} é um palindromo")
else:
    print(f"A palavra {palavra} não é um palindromo")
