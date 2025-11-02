import random

#DESAFIO 028
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
numero = int(input("Escolha um número de 0 a 5: ").strip())
numero_aleatorio = random.randint(0, 5)
print(f"Número sorteado {numero_aleatorio}")
if numero == numero_aleatorio:
  print("Parabéns você acertou!")
else:
  print("Você errou!")

'''
#DESAFIO 029
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
'''
velocidade = random.randint(10, 110)
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print(f"Velocidade atual {velocidade}Km/h. Você foi multado em R${multa:.2f}!")
else:
  print(f"Velocidade atual {velocidade}Km/h. Tenha uma boa viagem!")

'''
#DESAFIO 030
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
numero = int(input("Digite um número: ").strip())
par_ou_impar = numero % 2
if par_ou_impar == 0:
  print("PAR")
else:
  print("ÍMPAR")

'''
#DESAFIO 031
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
viagem = int(input("Distância da viagem: ").strip())
if viagem <= 200:
  preco = viagem * 0.50
  print(f"A distância da viagem é {viagem}Km e vai custar R${preco:.2f}")
else:
  preco = viagem * 0.45
  print(f"A distância da viagem é {viagem}Km e vai custar R${preco:.2f}")

'''
#DESAFIO 032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
ano = int(input("Digite um ano: ").strip())
case1 = ano % 4
case2 = ano % 100
case3 = ano % 400
if case1 == 0 and case2 != 0:
  print(f"O ano {ano} é bissexto.")
elif case1 == 0 and case2 == 0 and case3 == 0:
  print(f"O ano {ano} é bissexto.")
else:
  print(f"O ano {ano} não é bissexto.")

'''
#DESAFIO 033
#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
'''
numero01 = int(input("Primeiro número: ").strip())
numero02 = int(input("Segundo número: ").strip())
numero03 = int(input("Terceiro número: ").strip())
lista = [numero01, numero02, numero03]
ordenando = lista.sort()
print(f"Menor número: {lista[0]}\nMaior número: {lista[-1]}")

'''
#DESAFIO 034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input("Qual o seu salário? ").strip())
if salario > 1250:
  aumento = salario * 1.1
  print(f"O seu salário de R${salario:.2f} teve um aumento de 10% e agora é R${aumento:.2f}")
else:
  aumento = salario * 1.15
  print(f"O seu salário de R${salario:.2f} teve um aumento de 15% e agora é R${aumento:.2f}")

'''
#DESAFIO 035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
reta01 = float(input("Primeira reta: ").strip())
reta02 = float(input("Segunda reta: ").strip())
reta03 = float(input("Terceira reta: ").strip())
lista = [reta01, reta02, reta03]
ordenando = lista.sort()
resultado = lista[0] + lista[1] 
if resultado > lista[-1]:
  print("É possível fazer um triângulo")
else:
  print("Não é possível fazer um trinângulo")
'''