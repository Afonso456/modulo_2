frase= input("Insira uma frase:")
len(frase)
frase_invertida= ""
for i in range(len(frase) -1,-1,-1):
    frase_invertida = frase_invertida + frase[i]
if frase_invertida == frase:
    print(f"É palavra {frase} é um palindromo")
else:
    print(f"A palavra {frase} não é um palindromo")
