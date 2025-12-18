#DESAFIO 044
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- À vista dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros

preco = float(input("Preço do produto: R$ ").strip())
forma_pagamento = int(input("Digite 1 para pagar à vista em dinheiro ou cheque.\nDigite 2 para pagar à vista no cartão.\nDigite 3 para pagar em até 2x no cartão.\nDigite 4 para pagar em 3x ou mais no cartão.\nForma de pagamento escolhida: ").strip())

if forma_pagamento == 1:
  desconto = preco * 0.9
  print(f"Valor à pagar: R${desconto:.2f}")
elif forma_pagamento == 2:
  desconto = preco * 0.95
  print(f"Valor à pagar: R${desconto:.2f}")
elif forma_pagamento == 3:
  parcela = preco / 2
  print(f"Sua compra será parcelada em 2x de R${parcela:.2f}")
  print(f"Valor à pagar: R${preco:.2f}")
elif forma_pagamento == 4:
  juros = preco * 1.20
  total_parcela = int(input("Quantas parcelas? "))
  parcela = juros / total_parcela
  if total_parcela >= 3:
    print(f"Sua compra será parcelada em {total_parcela}x de R${parcela:.2f}")
    print(f"Valor à pagar: R${juros:.2f}")
  else:
    print("Parcela mínima de 3x. Tente novamente.")
else:
  print("[ERROR] Digite uma opção válida!")

