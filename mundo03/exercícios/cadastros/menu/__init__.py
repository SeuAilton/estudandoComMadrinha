from cadastros import adicionar
import os

def existencia(file):
  return os.path.exists(file)


def menu():
  while True:
    print()
    print(f"""{'-' * 30}
        Menu Principal
{'-' * 30}
\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas\033[m
\033[0;33m2\033[m - \033[0;34mCadastrar nova Pessoa\033[m
\033[0;33m3\033[m - \033[0;34mSair do sistema\033[m
{'-' * 30}
""")
    while True:
      try:
        escolha = int(input("\033[0;35mEscolha uma opção\033[m: ").strip())
        print()
        if 1 <= escolha <= 3:
          break
        else:
          print("\033[0;31m[ERRO]Digite uma opção válida!\033[m\n")
      except ValueError:
        print()
        print("\033[0;31m[ERRO]Digite um número inteiro!\033[m\n")
    if escolha == 1:
      if not existencia("cadastros.txt"):
        print("\033[0;33mSem pessoas cadastradas!\033[m")
      else:
        print("-" * 30)
        print(" \033[0;32mLista de pessoas cadastradas\033[m")
        print("-" * 30)
        with open("cadastros.txt", "r") as f:
          for lista in f:
            print(lista.rstrip())
    if escolha == 2:
      adicionar.cadastro()
    if escolha == 3:
      break


