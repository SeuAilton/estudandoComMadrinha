# DESAFIO 086
# Crie um programa que crie uma matriz de
# dimensão 3x3 e preencha com valores lidos pelo
# teclado.
# No final, mostre a matriz na tela, com a
# formatação correta.

lista = list()
numeros = list()

for n in range(0, 9):
  numeros.append(int(input("Número: ").strip()))
  lista.append(numeros[:])
  numeros.clear()

print(f"""
      [ {lista[0][0]} ] [ {lista[1][0]} ] [ {lista[2][0]} ]
      [ {lista[3][0]} ] [ {lista[4][0]} ] [ {lista[5][0]} ]
      [ {lista[6][0]} ] [ {lista[7][0]} ] [ {lista[8][0]} ]
      """)

