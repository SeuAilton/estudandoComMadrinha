#DESAFIO 018
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Ângulo: "))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print(f"Seno: {seno:.2f} \nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")
