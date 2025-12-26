# DESAFIO 074
# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla

from random import randint

tupla = tuple(randint(0, 100) for i in range(5))

print(tupla)

maior = max(tupla)
menor = min(tupla)

print(f"""Maior número: {maior}
Menor número: {menor}""")

