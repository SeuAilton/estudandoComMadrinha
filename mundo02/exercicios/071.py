#DESAFIO 071
#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor_em_caixa = [50, 20, 10, 1]
cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0

while True:
  saque = int(input("Valor a ser sacado: R$").strip())
  while saque > 0:
    if saque >= valor_em_caixa[0]:
      saque -= 50
      cedula_50 += 1
    elif saque >= valor_em_caixa[1]:
      saque -= 20
      cedula_20 += 1
    elif saque >= valor_em_caixa[2]:
      saque -= 10
      cedula_10 += 1
    elif saque >= valor_em_caixa[3]:
      saque -= 1
      cedula_1 += 1
  break

print(f"""Foram usadas: 
{cedula_50} cédulas de R$50.
{cedula_20} cédulas de R$20.
{cedula_10} cédulas de R$10.
{cedula_1} cédulas de R$01.""")
