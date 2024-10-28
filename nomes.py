n1= input("Insira o seu nome:")
n2= input("Insira o nome do seu amigo:")
t1=len(n1)
t2= len(n2)
if t1 > t2:
    print("O seu nome é o maior")
elif t1 < t2:
    print("O nome do seu amigo é maior")
else:
    print("Ambos os nome são iguais")
