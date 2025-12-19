#DESAFIO 068
#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitoria = 0

while True:
  jogador_numero = int(input("Escolha um número: ").strip())

  while True:
    jogador_par_impar = input("Escolha [P]par ou [I]ímpar: ").strip().upper()[0]
    if jogador_par_impar != "I" and jogador_par_impar != "P":
      print("[ERRO]Escolha uma opção válida!")
    else:
      break

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

#Resolução do professor.
'''
v = 0
while True:
  jogador = int(input("Diga um valor: "))
  computador = randint(0, 10)
  total = jogador + computador
  tipo = " "
  while tipo not in "PI":
    tipo = input("Par ou Ímpar? [P/I] ").strip().upper()[0]
  print(f"Você jogou {jogador} e o computador {computador}. Total de {total}")
  print(f"DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
  if tipo == "P":
    if total % 2 == 0:
      print("Você VENCEU!")
      v += 1
    else:
      print("Você PERDEU!")
      break
  elif tipo == "I":
    if total % 2 == 1:
      print("Você VENCEU!")
      v += 1
    else:
      print("Você PERDEU!")
      break
  print("Vamos jogar novamente...")
print(f"Foram {v} vitórias consecutivas.")
'''
