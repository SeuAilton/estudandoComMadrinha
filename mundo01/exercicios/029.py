#DESAFIO 029
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

import random

#velocidade = random.randint(10, 110)
velocidade = int(input("Velocidade: ").strip())
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print("-=-" *10)
  print(f"Velocidade atual {velocidade}Km/h.\nVocê foi multado em R${multa:.2f}!")
  print("-=-" *10)
else:
  print("-=-" *10)
  print(f"Velocidade atual {velocidade}Km/h.\nTenha uma boa viagem!")
  print("-=-" *10)
