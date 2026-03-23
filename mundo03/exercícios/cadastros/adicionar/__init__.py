def idade(msg):
  while True:
    try:
      numero = int(input(msg))
      if 0 < numero < 100:
        return numero
      else:
        print("\033[0;31m[ERRO]Digite uma idade válida!\033[m")       
    except ValueError:
      print("\033[0;31m[ERRO]Digite um número inteiro válido!\033[m")


def cadastro():
  while True:
    nome = input("Nome: ").strip().capitalize()
    if nome == "":
      print("\033[0;31m[ERRO]Digite um nome!\033[m")
    else:
      break
  idade_pessoa = idade("Idade: ")
  with open("cadastros.txt", mode="a", encoding="utf-8") as file:
    file.write(f"{nome:.<23}{idade_pessoa} anos\n")


