#DESAFIO 064
#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o a condição de parada 999).

soma = 0
contador = 0
numero = int(input("Digite um número [999 para parar]: ").strip())

while numero != 999:
  soma += numero
  contador += 1
  numero = int(input("Digite um número [999 para parar]: ").strip())

print(f"Foram digitador {contador} numeros.")
print(f"A soma entre os numeros digitados é: {soma}")

