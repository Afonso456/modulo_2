#Programa que indica se a password inserida pelo utilizador é valida ou não
a_m= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a_min= a_m.lower()
a_s= "!@£§€&#,;.:-_*"
a_n="0123456789"
ppass= input("Insira a sua password:")
TEM_M= False 
TEM_MIN= False
TEM_S= False
TEM_N= False

for letra in a_m:
    if letra in ppass:
        TEM_M= True
        break

for letra in a_min:
    if letra in ppass:
        TEM_MIN= True
        break

for letra in a_s:
    if letra in ppass:
        TEM_S= True
        break

for letra in a_n:
    if letra in ppass:
        TEM_N= True
        break

if TEM_M == True and TEM_MIN == True and TEM_S == True and TEM_N == True and len(ppass) >= 8:
    print("Palavra passe segura")
else:
    print("Palavra passe insegura")