#DESAFIO 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$ 1,00 = R$ 3,27

dinheiro = float(input("Dinheiro: R$ "))
conversao = dinheiro / 3.27
conversao_nova = dinheiro / 5.43
print(f"Convertido pra dólar = {conversao:.2f} \nConversão atual = {conversao_nova:.2f}")

