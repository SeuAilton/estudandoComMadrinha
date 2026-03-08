# DESAFIO 113
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leiaFloar() com a mesma funcionalidade.

def leiaInt(string, *args):
  while True:
    print(string, end=" ")
    try:
      numero = int(input(*args))
      if numero:
        break
    except ValueError:
      print("\033[0;31m[ERRO]Digite um número inteiro!\033[m")
  return numero


n = leiaInt("Digite um número:")
print(f"Você digitou o número {n}")

