pontos = 12
op= 0
infracao_leve= 0
infracao_mgrave= 0
infracao_grave= 0
while op != "4":
    print(f"Tem {pontos} pontos restantes")
    if pontos == 0:
        print("Perdeu a sua carta")
    print ("1.Muito Grave/2.Grave/3.Leve/4.Terminar")
    escolha= input("Insira a infração cometida:")
    if escolha == "1":
        pontos = pontos - 6
        infracao_mgrave= infracao_mgrave + 1
    if escolha == "2":
        pontos = pontos - 4
        infracao_grave = infracao_grave + 1
    if escolha == "3":
        if infracao_leve > 0:
            pontos = pontos - 1
        infracao_leve = infracao_leve + 1
    if (infracao_mgrave == 1 and infracao_grave == 1) or (infracao_grave == 2):
        pontos = 0
    if pontos < 0:
        pontos = 0