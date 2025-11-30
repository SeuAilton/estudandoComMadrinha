#DESAFIO 055
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior peso e o menor peso lidos.

maior = 0
menor = 0

for i in range(1, 6):
  peso = float(input(f"Peso da {i}ª pessoa: ").strip())
  if i == 1:
    maior = peso
    menor = peso
  if peso > maior:
    maior = peso
  elif peso < menor:
    menor = peso

print(f"""Maior peso: {maior:.1f}kg
Menor peso: {menor:.1f}kg""")
