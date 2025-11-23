#DESAFIO 031
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = int(input("Distância da viagem: ").strip())
if viagem <= 200:
  preco = viagem * 0.50
  print(f"A distância da viagem é {viagem}Km e vai custar R${preco:.2f}")
else:
  preco = viagem * 0.45
  print(f"A distância da viagem é {viagem}Km e vai custar R${preco:.2f}")
