# DESAFIO 106
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra "FIM", o programa se encerrará.
# OBS: use cores.
import pydoc

def titulo(msg, cor=0):
  tam = len(msg) + 4
  print(c[cor], end="")
  print("-" * tam)
  print(f"  {msg}  ")
  print("-" * tam)
  print(c[0], end="")


def ajuda():
  while True:
    titulo("SISTEMA DE AJUDA PyHELP", 4)
    escolha = input("Função ou Biblioteca > ")
    if escolha in "FIMfim":
      break
    else:
      doc = pydoc.render_doc(escolha)
      print(c[3], end="")
      print(doc)


c = ("\033[m",        # 0 - sem cores
     "\033[0;30;41m", # 1 - vermelho
     "\033[0;30;42m", # 2 - verde
     "\033[0;30;43m", # 3 - amarelo
     "\033[0;30;44m", # 4 - azul
     "\033[0;30;45m", # 5 - roxo
     "\033[7;30m"     # 6 - branco
     )


ajuda()

