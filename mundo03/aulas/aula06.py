#help() # ajuda do Python pode colocar algum parâmetro Ex.help(print)
#print(int.__doc__) # outra opção de ajuda print(parâmetro.__doc__)

def contador(i, f, p):
  """
  -> Faz uma contagem e mostra na tela.
  :param i: início da contagem
  :param f: fim da contagem
  :param p: passo da contagem
  :return: sem retorno
  """
  c = i
  while c <= f:
    print(f"{c}", end="..")
    c += p
  print("FIM!")


#contador(2,10,2)
#help(contador)

# Parâmetros opcionais

def somar1(a=0, b=0, c=0):
  s = a + b + c
  print(f"A soma vale {s}")


#somar1(3,2,5)
#somar1(8,4)
#somar1()

# Escopo

def teste(b):
  global a
  a = 8
  b += 4
  c = 2
  print(f"A dentro vale {a}")
  print(f"B dentro vale {b}")
  print(f"C dentro vale {c}")


a = 5
#teste(a)
#print(f"A fora vale {a}")


# Retorno de função

def somar2(a=0, b=0, c=0):
  s = a + b + c
  return s


r1 = somar2(3, 2, 5)
r2 = somar2(1, 7)
r3 = somar2(4)

#print(f"Meus cálculos deram {r1}, {r2} e {r3}")


# Fatorial

def fatorial(num=1):
  f = 1
  for c in range(num, 0, -1):
    f *= c
  return f


#n = int(input("Digite um número: ").strip())
#print(f"O fatorial de {n} é igual a {fatorial(n)}")

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
#print(f"Os resultados são {f1}, {f2} e {f3}")


# Função verifica se é par

def par(n=0):
  if n % 2 == 0:
    return True
  else:
    return False


num = int(input("Digite um número: ").strip())
if par(num):
  print(f"{num} é par!")
else:
  print(f"{num} é ímpar!")

