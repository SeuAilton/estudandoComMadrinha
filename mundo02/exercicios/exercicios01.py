from datetime import date

#DESAFIO 036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
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

'''
#DESAFIO 037
#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#- 1 para binário
#- 2 para octal
#- 3 para hexadecimal
'''
numero = int(input("Digite um número: ").strip())
escolha = int(input("Digite 1 para binário, 2 para octal, 3 para hexadecimal: ").strip())

if escolha == 1:
  print(f"O {numero} convertido para binário {numero:b}.")
elif escolha == 2:
  print(f"O {numero} convertido para octal {numero:o}.")
else:
  print(f"O {numero} convertido para hexadecimal {numero:x}.")

'''
#DESAFIO 038
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
'''
n1 = int(input("Digite um número: ").strip())
n2 = int(input("Digite outro número: ").strip())

if n1 > n2:
  print(f"O maior valor entre o {n1} e {n2} é {n1}")
elif n1 < n2:
  print(f"O maior valor entre o {n1} e {n2} é {n2}")
else:
  print(f"Entre {n1} e {n2} não existe valor maior, os dois são iguais")

'''
#DESAFIO 039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
ano = int(input("Ano de nascimento: ").strip())
ano_atual = date.today().year

if ano_atual - ano == 18:
  print("É hora de se alistar no exército.")
elif ano_atual - ano < 18:
  print("Ainda não está na hora de se alistar.")
else:
  print(f"Já passou {ano_atual - ano - 18} anos do prazo para se alistar.")

'''
#DESAFIO 040
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atigingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
'''
nota1 = float(input("Primeira nota: ").strip())
nota2 = float(input("Segunda nota: ").strip())
media = (nota1 + nota2) / 2

if media < 5:
  print(f"Média {media:.1f} REPROVADO!")
elif media >= 5 and media <= 6.9:
  print(f"Média {media:.1f} RECUPERAÇÃO!")
else:
  print(f"Média {media:.1f} APROVADO!")

'''
#DESAFIO 041
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a didade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JUNIOR
#- Até 20 anos: SÊNIOR
#- Acima: MASTER
'''
ano = int(input("Ano de nascimento: ").strip())
ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
  print(f"O aluno tem {idade} anos. MIRIM")
elif idade > 9 and idade <= 14:
  print(f"O aluno tem {idade} anos. INFANTIL")
elif idade > 14 and idade <= 19:
  print(f"O aluno tem {idade} anos. JUNIOR")
elif idade > 19 and idade <= 20:
  print(f"O aluno tem {idade} anos. SÊNIOR")
else:
  print(f"O aluno tem {idade} anos. MASTER")

'''
#DESAFIO 042
#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: todos os lados iguais
#- Isóceles: dois lados iguais
#- Escaleno: todos os lados diferentes

#DESAFIO 043
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do Peso
#- Entre 18.5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade mórbida

#DESAFIO 044
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- Á vista dinheiro/cheque: 10% de desconto
#- Á vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros

#DESAFIO 045
#Crie um programa que faça o computador jogar Jokenpô com você.