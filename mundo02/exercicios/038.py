#DESAFIO 038
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

n1 = int(input("Digite um número: ").strip())
n2 = int(input("Digite outro número: ").strip())

if n1 > n2:
  print(f"O maior valor entre o {n1} e {n2} é {n1}")
elif n1 < n2:
  print(f"O maior valor entre o {n1} e {n2} é {n2}")
else:
  print(f"Entre {n1} e {n2} não existe valor maior, os dois são iguais")
