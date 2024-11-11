#notebookLM
a= int(input("Insira o tamanho do lado:"))
b= int(input("Insira o tamanho do lado:"))
c= int(input("Insira o tamanho do lado:"))
if a <= 0 or b <= 0 or c <= 0 or a + b < c or a + c < b or b + c < a :
    print("O triangulo não é valido")
    if a == b and b == c:
        print("Equilatero")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Escaleno")
