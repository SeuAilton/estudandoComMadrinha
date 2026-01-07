# DESAFIO 078
# Faça um programa que leia 5 valores numéricos e guarde-os em
# uma lista.
# No final, mostre qual foi o maior e o menor valor digitados e as
# suas respectivas posições na lista.

lista = []
pMax = []
pMin = []

for count in range(0, 5):
  lista.append(int(input("Digite um número: ").strip()))

maior = max(lista) 
menor = min(lista)

for c, v in enumerate(lista):
  if v == maior:
    pMax.append(c)
  else:
    pMin.append(c)

print(f"O maior número é {maior} na posição {pMax}.")
print(f"O menor número é {menor} na posição {pMin}.")

