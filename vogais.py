frase= input("Insira a sua frase favorita:")
count= 0
for l in frase:
    print(l)
    if l in "aeiouAEIOU":
        count= count + 1
print("A frase indicada tem" ,count, "vogais")