# DESAFIO 105
# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def notas(*n, sit=False):
  """
  -> Função para analizar notas e situação de vários alunos.
  :param n: uma ou mais notas dos alunos
  :param sit: valor opcional, indicando se deve ou não adicionar a situação.
  :return: dicionário com várias informações sobre a situação da turma.
  """
#  r = dict()
#  r["total"] = len(n)
#  r["maior"] = max(n)
#  r["menor"] = min(n)
#  r["média"] = sum(n)/len(n)
#  if sit:
#    if r["média"] >= 7:
#      r["situação"] = "BOA"
#    elif r["média"] >= 5:
#      r["situação"] = "RAZOÁVEL"
#    else:
#      r["situação"] = "RUIM"
#  return r

  notas = []
  c = 0
  for numeros in n:
    notas.append(numeros)
    c += numeros
  quantidade = len(notas)
  maior = max(notas)
  menor = min(notas)
  media = c / quantidade
  dicionario = {"total": quantidade,
                "maior": maior,
                "menor": menor,
                "média": f"{media:.1f}"}
  if sit:
    if media >= 7:
      dicionario["situação"] = "BOA"
    elif media >= 5:
      dicionario["situação"] = "RAZOÁVEL"
    else:
      dicionario["situação"] = "RUIM"
  
  return dicionario


print(notas(4,5,5,5, sit=False))

