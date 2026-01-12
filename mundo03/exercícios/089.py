# DESAFIO 089
# Crie um programa que leia nome e duas notas
# de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo 
# a média de cada um e permita que o usuário possa 
# mostrar as notas de cada aluno individualmente.

alunos = list()
alunos_media = list()

while True:
  aluno = input("Nome do aluno: ").strip().capitalize()
  nota1 = int(input("Primeira nota: ").strip())
  nota2 = int(input("Segunda nota: ").strip())
  media = (nota1 + nota2) / 2
  alunos.append([aluno, [nota1, nota2], media])
  while True:
    continuar = input("Deseja continuar? [S/N]").strip().upper()[0]
    if continuar not in "SN":
      print("[ERRO]Digite um valor válido!")
    else:
      break
  if continuar == "N":
    break

for n in alunos:
  print(n[0], n[2])

while True:
  ver_notas = input("Deseja ver a nota de qual aluno? ").strip().capitalize()
  for a in alunos:
    if a[0] == ver_notas:
      print(a[0], a[1])
  while True:
    consulta = input("Deseja consultar outro aluno? [S/N]" ).upper().strip()[0]
    if consulta not in "SN":
      print("[ERRO]Digite um valor válido!")
    else:
      break
  if consulta == "N":
    break

