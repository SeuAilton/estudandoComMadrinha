# DESAFIO 102
# Crie uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.
from time import sleep

def fatorial(value, show=False):
  """
  -> Calcula o Fatorial de um número.
  :param value: O número a ser calculado.
  :param show: (opcional) Mostrar ou não a conta.
  :return: O valor do Fatorial de um número value.
  """
  resultado = 1
  c = 1
  processo = []
  while c <= value:
    resultado *= c
    processo.append(resultado)
    c += 1
  if show:
    print(f"O processo do fatorial de {value} é: ", end="")
    for v in processo:
      print(v, end="..", flush=True)
      sleep(0.5)
    print("FIM.")
  else:
    print(f"O fatorial de {value} é: {resultado}")


while True:
  numero = int(input("Digite um número: ").strip())
  fatorial(numero)
  while True:
    processo = input("Deseja mostrar o processo?[s/n] ").strip().lower()[0]
    if processo not in "sn":
      print("[ERRO]Digite uma opção válida!")
    else:
      if processo == "s":
        fatorial(numero, True)
        break
      else:
        break
  while True:
    continuar = input("Deseja ver outro número?[s/n]").strip().lower()[0]
    if continuar not in "sn":
      print("[ERRO]Digite uma opção válida!")
    else:
      break
  if continuar == "n":
    break

