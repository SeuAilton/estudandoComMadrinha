#DESAFIO 034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o seu salário? ").strip())
if salario > 1250:
  aumento = salario * 1.1
  print(f"O seu salário de R${salario:.2f} teve um aumento de 10% e agora é R${aumento:.2f}")
else:
  aumento = salario * 1.15
  print(f"O seu salário de R${salario:.2f} teve um aumento de 15% e agora é R${aumento:.2f}")
