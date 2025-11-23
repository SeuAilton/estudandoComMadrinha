#DESAFIO 015
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quantidade_Km = float(input("Quantidade de Km rodados: "))
dias_de_aluguel = int(input("Dias alugado: "))
preco_Km = quantidade_Km * 0.15
preco_dia = dias_de_aluguel * 60
total = preco_Km + preco_dia

print(f"Valor final do aluguel do carro: R${total:.2f}")
