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
                "média": f"{media:.2f}"}
  if sit:
    if media >= 7:
      dicionario["situação"] = "BOA"
      return dicionario
    if media >= 5:
      dicionario["situação"] = "RAZOÁVEL"
      return dicionario
    else:
      dicionario["situação"] = "RUIM"
      return dicionario
  else:
     return dicionario


print(notas(4,5,9,7,2,4, sit=True))

