#DESAFIO 052
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Número: ").strip())

controle = 0

for i in range(1, numero + 1):
  if numero % i == 0:
    controle += 1

if controle == 2:
  print(f"O número {numero} é primo.")
else:
  print(f"O número {numero} não é primo.")

