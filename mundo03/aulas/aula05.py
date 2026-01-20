def soma(a, b):
  print(f"A = {a} e B = {b}")
  s = a + b
  print(f"A soma A + B = {s}")


def contador(*num):
  for valor in num:
    print(f"{valor} ", end="")
  print("FIM!")
  tam = len(num)
  print(f"Recebi os valores {num} e ao todo são {tam} números")


def dobra(dst):
  pos = 0
  while pos < len(dst):
    dst[pos] *= 2
    pos += 1
    

def otasoma(*valor):
  s = 0
  for num in valor:
    s += num
  print(f"Somando os valores {valor} temos {s}")
  

a = 4
b = 5
s = a + b
print(s, "manual")
soma(4, 5)
soma(b=4, a=5)

a = 8
b = 9
s = a + b
print(s, "manual")
soma(8, 9)

a = 2
b = 1
s = a + b
print(s, "manual")
soma(2, 1)

contador(1, 2)
contador(3, 4, 5, 6)
contador(7, 8)
contador(9)

valores = [1, 2, 3, 4, 5, 6]
print(valores)
dobra(valores)
print(valores)

otasoma(1, 2)
otasoma(3, 4, 5)

