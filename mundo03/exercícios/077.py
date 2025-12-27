# DESAFIO 077
# Crie um programa que tenha uma tupla com várias
# palavras (não usar acentos). Depois disso, você
# deve mostre, para cada palavra, quais são as suas vogais.

palavras = ("preludio", "madrinha", "moka", "jubs", "lemos")
vogais = "aeiou"
vogais_encontradas = []

for palavra in palavras:
  for vogal in palavra:
    if vogal in vogais:
      vogais_encontradas.append(vogal)

