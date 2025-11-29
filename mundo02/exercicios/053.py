#DESAFIO 053
#Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").strip()

tratamento = frase.replace(" ", "").lower()

inversao = tratamento[::-1]

if tratamento == inversao:
  print(f'A frase "{frase}" é um palíndromo.')
else:
  print(f'A frase "{frase}" não é um palíndromo.')
