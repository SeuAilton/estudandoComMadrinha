def adicionar():
  nome = input("Nome: ").strip().capitalize()
  while True:
    try:
      idade = int(input("Idade: ").strip())
      if idade:
        break
    except ValueError:
      print("\033[0;31m[ERRO]Digite uma idade válida!\033[m")
  user = {}
  user["nome"] = nome
  user["idade"] = idade
  dicionario.append(user)
# TODO: Os itens do dicionário estão sendo substituidos
# pensar em uma forma de ir adicionando vários à lista

def menu():
  while True:
    print(f"""{'-' * 20}
Menu Principal
{'-' * 20}
1 - Ver pessoas cadastradas
2 - Cadastrar nova Pessoa
3 - Sair do sistema
""")
    while True:
      try:
        escolha = int(input("Escolha uma opção: ").strip())
        if escolha < 4 and escolha > 0:
          break
        else:
          print("\033[0;31m[ERRO]Digite uma opção válida!\033[m")
      except Exception:
        print("\033[0;31m[ERRO]Digite uma opção válida!\033[m")
    if escolha == 1:
      # TODO: Verificar se o dicionário está vazio e se tiver adicionar
      # uma mensagem adequada
      for index in range(len(dicionario)):
        for key in dicionario[index]:
          print(dicionario[index][key])
    if escolha == 2:
      adicionar()
    if escolha == 3:
      break


dicionario = [{}]

menu()

