#DESAFIO 058
#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

numero_escolhido = None
numero_aleatorio = randint(0, 10)
palpites = 0

while numero_escolhido != numero_aleatorio:
  numero_escolhido = int(input("Escolha um número de 0 a 10: ").strip())
  if numero_escolhido != numero_aleatorio:
    print("Você ERROU!\nTente novamente.")
    palpites += 1
print("-=-" *8)
print(f"Número sorteado foi: {numero_aleatorio}")
print("-=-" *8)
print("Você ACERTOU!")
print("-=-" *8)
print(f"Foram no total {palpites} palpites.")
print("-=-" *8)
