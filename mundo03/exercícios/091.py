# DESAFIO 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# em um dicionário. No final, coloque esse dicionário em ordem, sabendo
# que o vencedor tirou o maior número no dado.
from random import randint

jogadas = {"Jogador 1": randint(1,6),
           "Jogador 2": randint(1,6),
           "Jogador 3": randint(1,6),
           "Jogador 4": randint(1,6)}

ordem = dict(sorted(jogadas.items(), key=lambda item: item[1], reverse=True))

vencedor = max(jogadas.values())

print("-" * 19)

for k,v in ordem.items():
  print(f"{k} tirou: {v}")
  print("-" * 19)

for k,v in jogadas.items():
  if v == vencedor:
    print(f"{k} venceu!")

