#DESAFIO 016
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#    O número 6.127 tem a parte inteira 6.

import math

n1 = float(input("Número Real: "))
conversao = int(n1)
print(f"O número {n1} tem a parte inteira {conversao}.")
'''
n1 = float(input("Número Real: "))
conversao2 = math.trunc(n1)
print(f"O número {n1} tem a parte inteira {conversao2}.")
'''