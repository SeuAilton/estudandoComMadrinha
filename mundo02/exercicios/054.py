#DESAFIO 054
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (21anos)

maior = 0
menor = 0

for i in range(0, 7):
  idade = int(input("Idade: ").strip())
  if idade >= 21:
    maior += 1
  else:
    menor += 1

print(f"""{maior} pessoas são maiores de idade.
{menor} pessoas são menores de idade.""")
