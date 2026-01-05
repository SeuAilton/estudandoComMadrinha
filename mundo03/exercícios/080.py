# DESAFIO 080
# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []

for v in range(0, 5):
  numero = int((input("Número: ").strip()))
  if v == 0 or numero > lista[-1]:
    lista.append(numero)
  else:
    pos = 0
    while pos < len(lista):
      if numero <= lista[pos]:
        lista.insert(pos, numero)
        break
      pos += 1

print(lista)

