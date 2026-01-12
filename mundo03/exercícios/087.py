# DESAFIO 087
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = list()
controle = list()
par = 0
soma = 0

for n in range(0, 9):
  numeros = int(input("Número: ").strip())
  controle.append(numeros)
  lista.append(controle[:])
  if numeros % 2 == 0:
    par += numeros
  if n == 2 or n == 5 or n == 8:
    soma += numeros
  controle.clear()

print(f"""
      [ {lista[0][0]} ] [ {lista[1][0]} ] [ {lista[2][0]} ]
      [ {lista[3][0]} ] [ {lista[4][0]} ] [ {lista[5][0]} ]
      [ {lista[6][0]} ] [ {lista[7][0]} ] [ {lista[8][0]} ]
      """)

segunda_linha = lista[3] + lista[4] + lista[5]
maior_valor = max(segunda_linha)

print(f"Soma de todos os valores pares: {par}")
print(f"Soma dos valores da terceira coluna: {soma}")
print(f"Maior valor da segunda linha: {maior_valor}")

