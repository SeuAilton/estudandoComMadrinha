#DESAFIO 017
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input("Cateto oposto: "))
cateto_adjacente = float(input("Cateto adjacente: "))
hipotenusa = (pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
raiz = math.sqrt(hipotenusa)
print(f"Hipotenusa: {raiz:.2f}")
'''
cateto_oposto = float(input("Cateto oposto: "))
cateto_adjacente = float(input("Cateto adjacente: "))
hipotenusa2 = math.hypot(cateto_oposto, cateto_adjacente)
print(f"Hipotenusa: {hipotenusa2:.2f}")
'''