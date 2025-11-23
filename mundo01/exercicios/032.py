#DESAFIO 032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input("Digite um ano. Digite 0 pra analizar o ano atual: ").strip())

if ano == 0:
  ano_atual = date.today().year
  ano = ano_atual

case1 = ano % 4
case2 = ano % 100
case3 = ano % 400

if case1 == 0 and case2 != 0:
  print(f"O ano {ano} é bissexto.")
elif case1 == 0 and case2 == 0 and case3 == 0:
  print(f"O ano {ano} é bissexto.")
else:
  print(f"O ano {ano} não é bissexto.")
