def leiaDinheiro(string, *args):
  while True:
    print(string, end=" ")
    try:
      numero = input(*args)
      numero_tratado = numero.replace(",", ".")
      numero_final = float(numero_tratado)
      if numero_final:
        break
    except ValueError:
      print("\033[0;31m[ERRO]Digite um valor válido!\033[m")
  return numero_final


