#DESAFIO 045
#Crie um programa que faça o computador jogar Jokenpô com você.

import random
import emoji
from time import sleep

tesoura = emoji.emojize(":victory_hand:")
papel = emoji.emojize(":hand_with_fingers_splayed:")
pedra = emoji.emojize(":raised_fist:")

jogada = int(input(f"Digite 1 para jogar tesoura {tesoura} .\nDigite 2 para jogar papel {papel} .\nDigite 3 para jogar pedra {pedra}.\nJogada escolhida: ").strip())

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(.5)

lista = [tesoura, papel, pedra]

jogada_pc = random.choice(lista)

if jogada == 1:
  if jogada_pc == tesoura:
    print(f"Ambos jogaram {tesoura}. EMPATE")
  elif jogada_pc == papel:
    print(f"Você jogou {tesoura} e o pc jogou {papel} . VITÓRIA")
  else:
    print(f"Você jogou {tesoura} e o pc jogou {pedra}. DERROTA")
elif jogada == 2:
  if jogada_pc == tesoura:
    print(f"Você jogou {papel}  e o pc jogou {tesoura}. DERROTA")
  elif jogada_pc == papel:
    print(f"Ambos jogaram {papel} . EMPATE")
  else:
    print(f"Você jogou {papel}  e o pc jogou {pedra}. VITÓRIA")
elif jogada == 3:
  if jogada_pc == tesoura:
    print(f"Você jogou {pedra} e o pc jogou {tesoura} . VITÓRIA")
  elif jogada_pc == papel:
    print(f"Você jogou {pedra} e o pc jogou {papel} . DERROTA")
  else:
    print(f"Ambos jogaram {pedra}. EMPATE")
else:
  print("[ERROR] Jogada inválida. Por favor selecione uma jogada válida! [ERROR]")

