#DESAFIO 063
#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#Ex:
#0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input("Digite um número: ").strip())

a = 0
b = 1
c = 0

while c < n:
  print(a)
  proximo = a + b
  a = b
  b = proximo
  c += 1
