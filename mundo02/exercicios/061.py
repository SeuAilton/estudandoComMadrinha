#DESAFIO 061
#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Termo: ").strip())
razao = int(input("Razão: ").strip())

n = 0

while n < 10:
  trem = termo + razao * n
  n += 1
  print(trem)

