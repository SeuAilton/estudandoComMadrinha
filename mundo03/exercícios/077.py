# DESAFIO 077
# Crie um programa que tenha uma tupla com várias
# palavras (não usar acentos). Depois disso, você
# deve mostre, para cada palavra, quais são as suas vogais.

palavras = ("preludio", "madrinha", "moka", "jubs", "lemos")
vogais = "aeiou"

for palavra in palavras:
  print(f"\nNa palavra {palavra.capitalize()} temos: ",end="")
  for letra in palavra:
    if letra in vogais:
      print(letra, end=" ")

