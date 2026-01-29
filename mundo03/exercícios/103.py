# DESAFIO 103
# Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.

def ficha(jogador="Anônimo", gols="0"):
  print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")
  print("-" * 50)


print("-" * 50)
nome = input("Nome do jogador: ").strip().capitalize()
gols = input("Gols no campeonato: ").strip()

if nome == "":
  if gols == "":
    ficha()
  else:
    ficha(gols=gols)
else:
  if gols == "":
    ficha(nome)
  else:
    ficha(nome, gols)

