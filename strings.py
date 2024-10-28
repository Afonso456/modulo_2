#Funções para manipualar strings
nome= " ola mundo "
marca= 'ferarri'
varias_linhas= """
isto é uma string 
com varisa linhas 
"""

#tamanho da string
print(len(nome))

#converter para maisculas
print(marca.upper())
print(marca)
marca = marca.upper()
print(marca)

#converter para minusculas
marca= marca.lower()

#colocar a primerira letra em maiusculas
marca= marca.capitalize()
print(marca)

#remove os espaços em branco  no inicio e no final da string
print(nome.strip())
nome= nome.strip()
print(len(nome))
