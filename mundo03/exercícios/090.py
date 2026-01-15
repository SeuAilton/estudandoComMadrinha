# DESAFIO 090
# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura
# na tela.

dicionario = {}
alunos = []

while True:
  dicionario["nome"] = input("Nome do(a) aluno(a): ").strip().capitalize()
  dicionario["media"] = float(input("Média do(a) aluno(a): ").strip())
  dicionario["status"] = "aguardando..."
  if dicionario["media"] <= 5:
    dicionario["status"] = "REPROVADO!"
  elif dicionario["media"] < 7:
    dicionario["status"] = "RECUPERAÇÃO!"
  else:
    dicionario["status"] = "APROVADO!"
  alunos.append(dicionario.copy())
  dicionario.clear()
  while True:
    cont = input("Deseja continuar o cadastro?[S/N] ").strip().upper()[0]
    if cont not in "SN":
      print("[ERRO]Digite uma opção válida!")
    else:
      break
  if cont == "N":
    break

print("-" * 20)
for a in alunos:
  print(f"""Nome: {a["nome"]}
Média: {a["media"]}
Status: {a["status"]}""")
  print("-" * 20)

