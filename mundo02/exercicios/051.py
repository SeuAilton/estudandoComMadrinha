#DESAFIO 051
#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input("Termo: ").strip())
razao = int(input("Razão: ").strip())

final = termo + razao * 10 #fórmula = "an = a1 + r·(n-1)"

for i in range(termo, final, razao):
  print(i)
