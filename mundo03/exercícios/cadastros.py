def adicionar():
  nome = input("Nome: ").strip().capitalize()
  while True:
    try:
      idade = int(input("Idade: ").strip())
      if idade > 0 and idade < 100:
        break
      else:
        print("\033[0;31m[ERRO]Digite uma idade válida!\033[m")       
    except ValueError:
      print("\033[0;31m[ERRO]Digite uma idade válida!\033[m")
  dicionario["nome"] = nome
  dicionario["idade"] = idade
  pessoas.append(dicionario.copy())
  dicionario.clear()


def menu():
  while True:
    print()
    print(f"""{'-' * 30}
        Menu Principal
{'-' * 30}
\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas\033[m
\033[0;33m2\033[m - \033[0;34mCadastrar nova Pessoa\033[m
\033[0;32m3\033[m - \033[0;34mSair do sistema\033[m
{'-' * 30}
""")
    while True:
      try:
        escolha = int(input("\033[0;35mEscolha uma opção\033[m: ").strip())
        print()
        if escolha < 4 and escolha > 0:
          break
        else:
          print("\033[0;31m[ERRO]Digite uma opção válida!\033[m")
      except Exception:
        print("\033[0;31m[ERRO]Digite uma opção válida!\033[m")
    if escolha == 1:
      if len(pessoas) == 0:
        print("\033[0;33mSem pessoas cadastradas!\033[m")
      else:
        print("-" * 30)
        print(" \033[0;32mLista de pessoas cadastradas\033[m")
        print("-" * 30)
      for a in pessoas:
        print(f"{a['nome']:.<22}", end=" ")
        print(f"{a['idade']} anos")
    if escolha == 2:
      adicionar()
    if escolha == 3:
      break


dicionario = {}
pessoas = []

