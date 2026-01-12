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
maior = menor = 0
pesados = []
leves = []

while True:
  lista_info.append(input("Nome: ").strip())
  lista_info.append(float(input("Peso: ").strip()))
  if len(lista) == 0:
    maior = menor = lista_info[1]
  else:
    if lista_info[1] > maior:
      maior = lista_info[1]
    if lista_info[1] < menor:
      menor = lista_info[1]
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
  if d[1] == maior:
    pesados.append(d[0])
  if d[1] == menor:
    leves.append(d[0])

print(f"As pessoas mais pesadas são: {pesados}")
print(f"As pessoas mais leves são: {leves}")
print(f"Foram cadastradas {cadastros} pessoas.")

