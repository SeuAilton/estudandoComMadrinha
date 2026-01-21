# DESAFIO 096
# Faça um programa que tenha uma função chamada área(), que receba
# as dimensões de um terreno retangular(largura e comprimento) e
# mostre a área do terreno.

def area(largura, comprimento):
  metro_quadrado = largura * comprimento
  return metro_quadrado

larg = float(input("Largura:(m²) ").strip())
comp = float(input("Comprimento:(m²) ").strip())

print(f"O terreno possui uma área de {area(larg, comp):.1f}m².")

