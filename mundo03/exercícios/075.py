# DESAFIO 075
# Desenvolva um programa que leia quatro valores pelo
# teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

#tupla = tuple(int(input("Número: ").strip()) for x in range(4))

tupla = (int(input("Número: ").strip()),
         int(input("Número: ").strip()),
         int(input("Número: ").strip()),
         int(input("Número: ").strip()))

valor9 = tupla.count(9)
if 3 in tupla:
  valor3 = tupla.index(3)
else:
  valor3 = 0
pares = tuple(n for n in tupla if n % 2 == 0)

print(f"""Tupla gerada: {tupla}
O número 9 apareceu {valor9} vezes.
O número 3 foi digitado primeiro na posição {valor3}.
Os números pares digitados foram: {pares}""")

