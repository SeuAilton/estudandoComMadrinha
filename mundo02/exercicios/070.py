#DESAFIO 070
#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#c) Qual é o nome do produto mais barato.

soma = caro = barato = 0
mais_barato = ""

while True:
  produto = input("Digite o nome do produto: ").strip().lower()
  preco = float(input("Valor do produto: R$").strip())

  if soma == 0 or preco < barato:
    mais_barato = produto
    barato = preco
  
  soma += preco

  if preco > 1000:
    caro += 1

  while True:
    continuar = input("Deseja continuar o cadastro dos produtos? [S/N] ").strip().upper()[0]
    if continuar != "S" and continuar != "N":
      print("[ERRO] Digite uma opção válida.")
    else:
      break

  if continuar == "N":
    break

print(f"Total gasto na compra: R${soma:.2f}")
print(f"Produtos que custam mais de R$1000,00: {caro}")
print(f"Produto mais barato: {mais_barato.capitalize()}")

