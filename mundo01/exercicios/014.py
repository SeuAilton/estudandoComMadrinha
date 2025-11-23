#DESAFIO 14
#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input("Temperatura em °C: "))
conversao = celsius * 9 / 5 + 32

print(f"A conversão: {conversao}°F")
