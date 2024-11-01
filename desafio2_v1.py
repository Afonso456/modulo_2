#programa que le os tempos de cada volta em 5 voltas
total= 0
for i in range (5):
    tempo= int(input("Insira o tempo das voltas:"))
    total= total + tempo
print(f"Demorou {total} minutos a fazer as cinco voltas")