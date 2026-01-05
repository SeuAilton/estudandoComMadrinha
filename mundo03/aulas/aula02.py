num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)
if 4 in num:
  num.remove(4)
else:
  print("Não tem o número 4")
print(f"A lista tem {len(num)} elementos.")

valores = []
valores.append(1)
valores.append(2)
valores.append(3)

for v in valores:
  print(f"{v}...", end="")

for c, v in enumerate(valores):
  print(f"\nNa posição {c} tem o valor {v}!")

numeros = list()

for cont in range(0, 5):
  numeros.append(int(input("Digite um valor: ").strip()))

print(numeros)

a = [1, 2, 3, 4]
b = a
b[2] = 8
c = a[:]
c[2] = 5

print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")
print(f"Lista A: {a}")

