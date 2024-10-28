segundos = 0
minutos = 0
musicas = 0
duracao_total = 0
while musicas == 0:
    musicas= int(input("Insira uma nova musica:"))
    if segundos >= 0 and segundos <= 6000:
        duracao_total = duracao_total + musicas 
        minutos= duracao_total // 60 
        segundos= duracao_total % 60
        continue
    else:
        print("O tempo inserido é invalido")

print(f"A duração total é de {minutos}:{segundos}")