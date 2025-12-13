#DESAFIO 060
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex:
#5! = 5x4x3x2x1 = 120

n = int(input("Digite um número: ").strip())
validador = 1
contador = 1

while validador <= n:
  contador *= validador
  validador += 1

print(f"{n}! = {contador}")
