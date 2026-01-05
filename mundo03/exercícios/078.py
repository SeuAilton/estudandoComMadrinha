# DESAFIO 078
# Faça um programa que leia 5 valores numéricos e guarde-os em
# uma lista.
# No final, mostre qual foi o maior e o menor valor digitados e as
# suas respectivas posições na lista.

lista = []

pMax = 0
pMin = 0

for count in range(0, 5):
  lista.append(int(input("Digite um número: ").strip()))

maior = max(lista) 
menor = min(lista)

for c, v in enumerate(lista):
  if c == 0:
    pMax = c
    pMin = c
  elif v < pMin:
    pMin = c
  else:
    pMax = c

print(f"O maior número é {maior} na posição {pMax}.")
print(f"O menor número é {menor} na posição {pMin}.")

