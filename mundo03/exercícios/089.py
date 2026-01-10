# DESAFIO 089
# Crie um programa que leia nome e duas notas
# de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo 
# a média de cada um e permita que o usuário possa 
# mostrar as notas de cada aluno individualmente.

alunos = list()
alunos_media = list()
c0 = list()
c1 = list()
c2 = list()
c3 = list()

while True:
  aluno = input("Nome do aluno: ").strip().capitalize()
  nota1 = int(input("Primeira nota: ").strip())
  nota2 = int(input("Segunda nota: ").strip())
  media = (nota1 + nota2) / 2
  c3.append(media)
  c2.append(nota1)
  c2.append(nota2)
  c1.append(aluno)
  c1.append(c2[:])
  c0.append(aluno)
  c0.append(c3[:])
  alunos.append(c1[:])
  alunos_media.append(c0[:])
  c3.clear()
  c2.clear()
  c1.clear()
  c0.clear()
  while True:
    continuar = input("Deseja continuar? [S/N]").strip().upper()[0]
    if continuar not in "SN":
      print("[ERRO]Digite um valor válido!")
    else:
      break
  if continuar == "N":
    break

for n in alunos_media:
  print(n)

while True:
  ver_notas = input("Deseja ver a nota de qual aluno? ").strip().capitalize()
  for a in alunos:
    if a[0] == ver_notas:
      print(a)
  while True:
    consulta = input("Deseja consultar outro aluno? [S/N]" ).upper().strip()[0]
    if consulta not in "SN":
      print("[ERRO]Digite um valor válido!")
    else:
      break
  if consulta == "N":
    break

