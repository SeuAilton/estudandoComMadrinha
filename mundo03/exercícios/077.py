# DESAFIO 077
# Crie um programa que tenha uma tupla com várias
# palavras (não usar acentos). Depois disso, você
# deve mostre, para cada palavra, quais são as suas vogais.

palavras = ("Preludio", "Madrinha", "Moka", "Jubs", "Lemos")
vogais = "aeiou"

for palavra in palavras:
  print(f"\nNa palavra {palavra.capitalize()} temos: ",end="")
  for letra in palavra:
    if letra.lower() in vogais:
      print(letra, end=" ")

