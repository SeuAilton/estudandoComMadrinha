#DESAFIO 039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input("Ano de nascimento: ").strip())
ano_atual = date.today().year
idade = ano_atual - ano

if idade == 18:
  saldo = idade - 18
  print("É hora de se alistar no exército.")
  print(f"Você deverá se alistar no ano de {ano_atual + saldo}.")
elif idade < 18:
  saldo = 18 - idade
  print("Ainda não está na hora de se alistar.")
  print(f"Seu alistamento será em {saldo} anos.")
  print(f"Você deverá se alistar no ano de {ano_atual + saldo}.")
else:
  print(f"Já passou {idade - 18} anos do prazo para se alistar.")
