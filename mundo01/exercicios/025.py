#DESAFIO 025
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Nome: ").strip()
nome_maiusculo = nome.upper()
achando_o_silva = nome_maiusculo.find("SILVA")
if achando_o_silva == -1:
  print(f"O nome {nome} não tem Silva.")
else:
  print(f"O nome {nome} tem Silva.")
