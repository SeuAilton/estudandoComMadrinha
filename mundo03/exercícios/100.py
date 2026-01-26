# DESAFIO 100
# Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primera função vai sortear
# 5 números e vai colocá-los dentro de uma lista e a segunda função
# vai mostrar a soma entre todos os valores PARES sorteados pela
# função anterior.

from random import randint
from time import sleep

def sorteia(lista):
  print("Os números sorteados foram: ", end="")
  while len(numeros_sorteados) < 5:
    n = randint(1, 100)
    lista.append(n)
    print(f"{n}", end=" ", flush=True)
    sleep(0.3)
  print()


def somaPar(lista):
  pares = 0
  for v in lista:
    if v % 2 == 0:
      pares += v
  print(f"A soma dos números pares é: {pares}")
 


numeros_sorteados = []

sorteia(numeros_sorteados)
somaPar(numeros_sorteados)

