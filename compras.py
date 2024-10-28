for i in range (1):
    orcamento = float(input("Insira o orçamento:"))
    capacidade= float(input("Insira a capacidade maxima de carga em KG:"))
while orcamento > 0 and capacidade > 0:
    preco= float(input("Insira o preço do produto:"))
    if preco == 0:
        break 
    peso= float(input("Insira o peso do produto:"))
    if preco < orcamento and capacidade < peso:
        print("Não tem dinheiro ou o produto é muito pesado")
    else:
        orcamento = orcamento - preco
        capacidade = capacidade - peso
        print(f"Ainda tem {orcamento} e ainda pode carregar mais{capacidade} Kg")
    print("As suas compras acabaram")