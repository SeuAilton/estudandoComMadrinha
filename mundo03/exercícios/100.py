# DESAFIO 100
# Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primera função vai sortear
# 5 números e vai colocá-los dentro de uma lista e a segunda função
# vai mostrar a soma entre todos os valores PARES sorteados pela
# função anterior.

from random import randint

numeros_sorteados = []

def sorteia():
  while len(numeros_sorteados) < 5:
    numeros_sorteados.append(randint(1, 100))


def somaPar():
  pares = 0
  for v in numeros_sorteados:
    if v % 2 == 0:
      pares += v
  return pares


sorteia()

print(f"Os números sorteados foram: {numeros_sorteados}")
print(f"A soma dos números pares é: {somaPar()}")

