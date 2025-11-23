#DESAFIO 037
#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#- 1 para binário
#- 2 para octal
#- 3 para hexadecimal

numero = int(input("Digite um número: ").strip())
escolha = int(input("Digite 1 para binário, 2 para octal, 3 para hexadecimal: ").strip())

if escolha == 1:
  print(f"O {numero} convertido para binário {numero:b}.")
elif escolha == 2:
  print(f"O {numero} convertido para octal {numero:o}.")
else:
  print(f"O {numero} convertido para hexadecimal {numero:x}.")
