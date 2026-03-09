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
      print("\033[0;31m[ERRO]Digite um número inteiro válido!\033[m")
  return numero


def leiaFloat(string, *args):
  while True:
    print(string, end=" ")
    try:
      numero = input(*args)
      numero_tratado = numero.replace(",", ".")
      numero_final = float(numero_tratado)
      if numero_final:
        break
    except ValueError:
      print("\033[0;31m[ERRO]Digite um número decimal válido!\033[m")
  return numero_final


i = leiaInt("Digite um número inteiro:")
f = leiaFloat("Digite um número decimal:")
print(f"Você digitou o número inteiro {i} e o número decimal {f:.1f}")

