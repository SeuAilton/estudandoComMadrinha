#DESAFIO 12
# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Preço: R$ "))
desconto = preco * (1 - 0.05)
print(f"Novo preço: R$ {desconto:.2f}")
