cont= 0
cont1= 0
for _ in range(10):
    letra=str(input("Insira vogais:"))
    letra= letra .strip()
    if len(letra) != 1:
        print("So pode inserir uma letra")
    else:
        if letra in "aeiouAEIOU":
            cont = cont + 1
            cont1 = cont1 +1 
print(f"{cont1} não são vogais")
print(f"{cont} são vogais")