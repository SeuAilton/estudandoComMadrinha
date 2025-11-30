#DESAFIO 054
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (21anos)

from datetime import date

ano = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
  idade = int(input(f"Ano de nascimento da {i}° pessoa: ").strip())
  if ano - idade >= 21:
    maior += 1
  else:
    menor += 1

print(f"""{maior} pessoas são maiores de idade.
{menor} pessoas são menores de idade.""")
