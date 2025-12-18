#DESAFIO 036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input("Valor da casa: R$").strip())
salario = float(input("Salário: R$").strip())
anos = int(input("Anos para pagar: ").strip())

prestacao =  valor_da_casa / (anos * 12)

if prestacao < salario * 0.3:
  print(f"Valor da prestação é R${prestacao:.2f}")
  print("Impréstimo aprovado!")
else:
  print(f"Valor da prestação é R${prestacao:.2f}")
  print("Impréstimo negado!")
  
