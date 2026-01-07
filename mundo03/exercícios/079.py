# DESAFIO 079
# Crie um programa onde o usuário possa digitar valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []

while True:
  numero = int(input("Número: ").strip())
  if numero not in lista:
    lista.append(numero)
  else:
    print("Número repetido!")
  while True:
    continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if continuar not in "SN":
      print("[ERRO]Digite um valor válido!")
    else:
      break
  if continuar == "N":
    break

lista_ordenada = lista.sort()

print(lista)

