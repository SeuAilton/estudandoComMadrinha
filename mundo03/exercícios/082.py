# DESAFIO 082
# Crie um programa que vai ler vários números e colocar em
# uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listap = []
listai = []

while True:
  numero = int(input("Digite um número: ").strip())
  lista.append(numero)
  if numero % 2 == 0:
    listap.append(numero)
  elif numero % 2 == 1:
    listai.append(numero)
  while True:
    continuar = input("Desaja continuar? [S/N]").strip().upper()[0]
    if continuar not in "SN":
      print("[ERRO]Digite uma opção válida!")
    else:
      break
  if continuar == "N":
    break

print(lista)
print(listap)
print(listai)

