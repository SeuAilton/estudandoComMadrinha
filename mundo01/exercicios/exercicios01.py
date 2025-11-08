#DESAFIO 01
#Crie um programa que escreva "Olá, Mundo!" na tela.
#print("Olá, Mundo!")

#DESAFIO 02
#Crie umm programa que colete o nome do usuário e dê as boas vindas.
#nome = input("Escreva seu nome: ")
#print("É um prazer te conhecer,", nome)
#print(f"É um prazer te conhecer, {nome}")

#DESAFIO 03
#Crie um programa que leia dois números e mostre a some entre eles.
n1 = int(input("Número01: "))
n2 = int(input("Número02: "))
soma = n1 + n2
print(f"A soma de {n1} e {n2} é {soma}")

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
