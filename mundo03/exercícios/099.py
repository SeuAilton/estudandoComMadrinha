# DESAFIO 099
# Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles
# é o maior
from time import sleep

def maior(*num):
  return list(map(max, num))


n = [[1, 2, 3, 4, 5],[6, 7, 8, 9],[10, 11, 12], [13, 14], [15]]
c = 0

print("-" * 40)
while c < len(n):
  print("Analizando os valores passados...")
  for v in n[c]:
    print(v, end=" ", flush=True)
    sleep(0.3)
  print()
  print(f"Foram informados {len(n[c])} valores ao todo.")
  print(f"O maior valor informado foi {maior(n[c])}")
  print("-" * 40)
  c += 1

