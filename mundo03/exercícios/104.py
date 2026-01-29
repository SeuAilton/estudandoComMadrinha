# DESAFIO 104
# Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante à função input() do Python, só que fazendo a 
# validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaInt("Digite um n")

def leiaInt(string, *args):
  while True:
    print(string, end=" ")
    try:
      numero = int(input(*args))
      if numero:
        break
    except ValueError:
      print("[ERRO]Digite um número inteiro!")
  return numero


n = leiaInt("Digite um número:")
print(f"Você digitou o número {n}")

