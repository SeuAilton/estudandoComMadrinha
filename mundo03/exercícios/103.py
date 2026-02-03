# DESAFIO 103
# Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.

def ficha(jogador=None, gols=None):
  if jogador is None or jogador == "":
    jogador = "Anônimo"
  if gols is None or gols == "":
    gols = 0
  return f"O jogador {jogador} fez {gols} gols(s) no campeonato."


nome = input("Nome do jogador: ").strip().capitalize()
gols = input("Gols no campeonato: ").strip()

print(ficha(nome, gols))

