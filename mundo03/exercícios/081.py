# DESAFIO 081
# Crie um programa que vai ler vários números e colocar em
# uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
  numero = lista.append(int((input("Número: ").strip())))
  while True:
    continuar = input("Deseja continuar? [S/N]").strip().upper()[0]
    if continuar != "S" and continuar != "N":
      print("[ERRO]Digite um valor válido!")
    else:
      break
  if continuar == "N":
    break

tamanho = len(lista)
crescente = lista.sort()
decrescente = lista[::-1]

if 5 in lista:
  print("Tem o número 5 na lista.")
else:
  print("Não foi digitado nenhum número 5.")

print(f"Foram digitados {tamanho} números.")
print(decrescente)

