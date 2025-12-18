#DESAFIO 065
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

validacao = "S"
soma = 0
quantidade = 0
maior = 0
menor = 0

while validacao == "S":
  numero = int(input("Digite um número: ").strip())
  validacao = input("Deseja continuar [S/N]? ").strip().upper()
  soma += numero
  quantidade += 1
  if quantidade == 1:
    maior = numero
    menor = numero
  if maior < numero:
    maior = numero
  elif menor > numero:
    menor = numero

media = soma / quantidade

print(f"A média entres os valores digitados foi {media:.1f}")
print(f"O maior número digitado: {maior}")
print(f"Menor número digitado: {menor}")

