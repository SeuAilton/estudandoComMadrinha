# DESAFIO 084
# Faça um programa que leia nome e peso de várias
# pessoas, guardando tudo em uma lista. No final,
# mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = list()
lista_info = list()
cadastros = 0
pesadas = list()
leves = list()

while True:
  lista_info.append(input("Nome: ").strip())
  lista_info.append(float(input("Peso: ").strip()))
  lista.append(lista_info[:])
  lista_info.clear()
  while True:
    continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if continuar not in "SN":
      print("[ERRO]Escolha uma opção válida!")
    else:
      break
  if continuar == "N":
    break

for d in lista:
  if d[0]:
    cadastros += 1

mais_pesadas = max(lista)
mais_leves = min(lista)

for v in lista:
  if v[1] == mais_pesadas[1]:
    pesadas.append(v[0])
  elif v[1] == mais_leves[1]:
    leves.append(v[0])

print(lista)
print(f"Foram cadastradas {cadastros} pessoas.")
print("As pessoas mais pesadas são: \n", pesadas)
print("As pessoas mais leves são: \n", leves)

