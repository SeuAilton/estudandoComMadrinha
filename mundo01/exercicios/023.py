#DESAFIO 023
#Faça um programa que leio um número de 0 a 9999 e mostre no tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#    unidade: 4
#    dezena: 3
#    centena: 8
#    milhar: 1

numero = int(input("Número: "))

if numero > 0 and numero <= 9999:
  unidade = numero % 10
  dezena = numero // 10 % 10
  centena = numero // 100 % 10
  milhar = numero // 1000 % 10
  print(f"unidade: {unidade}")
  print(f"dezena: {dezena}")
  print(f"centena: {centena}")
  print(f"milhar: {milhar}")
else:
  print("[ERROR]Digite um número entre 0 e 9999!")
