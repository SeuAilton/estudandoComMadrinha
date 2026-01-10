# DESAFIO 088
# Faça um programa que ajude um jogador da 
# MEGA SENA a criar palpites. O programa vai 
# perguntar quantos jogos serão gerados e vai 
# sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint

lista = list()
controle = list()
jogos = int(input("Quantos jogos? ").strip())

for n in range(0, jogos):
  while True:
    numero = randint(1, 60)
    if numero not in lista:
      controle.append(numero)
    if len(controle) == 6:
      lista.append(controle[:])
      controle.clear()
      print(f"Jogo {n+1}: {lista[n]}")
      break

