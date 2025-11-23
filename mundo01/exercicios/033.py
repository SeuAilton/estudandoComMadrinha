#DESAFIO 033
#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

numero01 = int(input("Primeiro número: ").strip())
numero02 = int(input("Segundo número: ").strip())
numero03 = int(input("Terceiro número: ").strip())
lista = [numero01, numero02, numero03]
ordenando = lista.sort()
print(f"Menor número: {lista[0]}\nMaior número: {lista[-1]}")
