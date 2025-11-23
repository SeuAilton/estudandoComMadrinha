#DESAFIO 022
#Crie um programa que leia o nome complero de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas as letas minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

nome = input("Nome: ").strip()
maiusculo = nome.upper()
minusculo = nome.lower()
separando_o_nome = nome.split()
tirando_os_espacos = "".join(separando_o_nome)
calculando_quantas_letras = len(tirando_os_espacos)
pegando_o_primeiro_nome = nome.split()[0]
quantas_letras_primeiro_nome = len(pegando_o_primeiro_nome)
print(maiusculo)
print(minusculo)
print(calculando_quantas_letras)
print(quantas_letras_primeiro_nome)

'''
nome = input("Nome: ").strip()
print(f"Nome maúsculo {nome.upper()}")
print(f"Nome minúsculo {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(" ")} letras.")
print(f"Seu primeiro nome tem {nome.find(" ")} letras.")
'''