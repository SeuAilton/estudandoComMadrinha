# DESAFIO 106
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra "FIM", o programa se encerrará.
# OBS: use cores.
import pydoc

def ajuda():
  while True:
    print("-" * 25)
    print("Sistema de ajuda PyHelp")
    print("-" * 25)
    escolha = input("Função ou Biblioteca > ")
    if escolha in "FIMfim":
      break
    else:
      doc = pydoc.render_doc(escolha)
      print(doc)


ajuda()

