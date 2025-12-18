#DESAFIO 053
#Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").strip().lower()

tratamento = frase.replace(" ", "")

inversao = tratamento[::-1]

if tratamento == inversao:
  print(f'A frase "{frase.capitalize()}" é um palíndromo.')
else:
  print(f'A frase "{frase.capitalize()}" não é um palíndromo.')

#Resolução Curso em Vídeo
'''
frase = input("Digite uma frase: ").strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]
if inverso == junto:
  print("É um palíndromo!")
else:
  print("Não é um palíndromo!")
'''

