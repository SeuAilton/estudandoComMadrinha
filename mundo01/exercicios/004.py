#DESAFIO 04
#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

coisa = input("Digita um trem ai: ")
print(type(coisa))
print(coisa.isalnum())
print(coisa.isdecimal())
print(coisa.isalpha())
print(coisa.islower())
print(coisa.isupper())
print(coisa.isdigit())