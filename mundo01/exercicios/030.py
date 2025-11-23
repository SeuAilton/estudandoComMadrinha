#DESAFIO 030
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um número: ").strip())
par_ou_impar = numero % 2
if par_ou_impar == 0:
  print("PAR")
else:
  print("ÍMPAR")
