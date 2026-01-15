# DESAFIO 94
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

dados = {}
cadastro = []
mulheres = []
acima_da_media = []
total_idade = 0

while True:
  nome = input("Nome: ").strip().capitalize()
  while True:
    sexo = input("Sexo:[M/F] ").strip().upper()[0]
    if sexo not in "MF":
      print("[ERRO]Digite uma opção válida!")
    else:
      break
  idade = int(input("Idade: ").strip())
  total_idade += idade
  dados["nome"] = nome
  dados["sexo"] = sexo
  dados["idade"] = idade
  if sexo == "F":
    mulheres.append(dados.copy())
  cadastro.append(dados.copy())
  dados.clear()
  while True:
    continuar = input("Deseja continuar?[S/N] ").strip().upper()[0]
    if continuar not in "SN":
      print("[ERRO]Digite uma opção válida")
    else:
      break
  if continuar == "N":
    break

total_cadastro = len(cadastro)
media = total_idade / total_cadastro

for v in cadastro:
  if v["idade"] >= media:
    acima_da_media.append(v)
    
print(f"Foram cadastradas {total_cadastro} pessoas.")
print(f"Média de idade do grupo: {media:.1f}.")

print("-" * 3, "MULHERES", "-" * 3)
print("-" * 10)
for v in mulheres:
  print(f"{v["nome"]}")
  print("-" * 10)
  
print("-" * 3, "ACIMA DA MÉDIA", "-" * 3)
print("-" * 10)
for v in acima_da_media:
  print(f"{v["nome"]}: {v["idade"]}")
  print("-" * 10)

