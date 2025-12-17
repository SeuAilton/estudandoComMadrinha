#DESAFIO 068
#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitoria = 0

while True:
  while True:
    jogador_par_impar = input("Escolha [P]par ou [I]ímpar: ").strip().upper()[0]
    if jogador_par_impar != "I" and jogador_par_impar != "P":
      print("[ERRO]Escolha uma opção válida!")
    else:
      break

  jogador_numero = int(input("Escolha um número: ").strip())

  computador = randint(1, 2)

  soma = jogador_numero + computador
  
  if soma % 2 == 0:
    if jogador_par_impar == "P":
      print(f"O número sorteado foi: {soma}.")
      print("Parabéns você venceu!")
      vitoria += 1
    else:
      print(f"O número sorteado foi: {soma}.")
      print("Você perdeu!")
      break
  else:
    if jogador_par_impar == "I":
      print(f"O número sorteado foi: {soma}.")
      print("Parabéns você venceu!")
      vitoria += 1
    else:
      print(f"O número sorteado foi: {soma}.")
      print("Você perdeu!")
      break

print(f"No total foram {vitoria} vitorias consecutivas.")
