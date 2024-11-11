import random
a_m= "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ"
ppass= ""
a_min= a_m.lower()
a_s= "!@£§€&#,;.:-_*"
a_n="0123456789"
for i in range (2):
    pos= random.randint(0,len(a_m))
    ppas= ppass + a_m[pos]
for i in range(2):
    pos= random.randint(0, len(a_min))
    ppass= ppass + a_min[pos]
print(ppass)
#TODO continuar aqui