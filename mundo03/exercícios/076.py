# DESAFIO 076
# Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos
# preços, na sequência.
# No final, mostre uma listagem de preços, organizando
# os dados em forma tubular.

produto = ("Linguiça", 69, "Pão de queijo", 4, 
           "Goiabada", 20, "Doce de leite", 10)

for count in range(0,len(produto),2):
  comida = produto[count]
  valor = produto[count+1]
  print(f"{comida:.<30} R${valor:>5.2f}")


