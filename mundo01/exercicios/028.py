#DESAFIO 028
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

numero = int(input("Escolha um número de 0 a 5: ").strip())
numero_aleatorio = random.randint(0, 5)
print("PROCESSANDO...")
sleep(2)
print("-=-" *8)
print(f"Número sorteado {numero_aleatorio}")
print("-=-" *8)
if numero == numero_aleatorio:
  print("Parabéns você acertou!")
else:
  print("Você errou!")
print("-=-" *8)
