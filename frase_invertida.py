frase= input("Insira uma frase:")
len(frase)
frase_invertida= ""
for i in range(len(frase) -1,-1,-1):
    frase_invertida = frase_invertida + frase[i]
    print(frase_invertida)