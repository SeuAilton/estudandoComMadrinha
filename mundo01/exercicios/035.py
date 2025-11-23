#DESAFIO 035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

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
