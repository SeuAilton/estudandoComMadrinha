'''for c in range(1, 10):
  print(c)
print("Fim")
'''
'''c = 1

while c < 10:
  print(c)
  c += 1
print("Fim")'''

'''for c in range(1, 5):
  input("Digite um valor: ")
print("Fim")'''

'''c = 1

while c != 0:
  c = int(input("Digite um número: "))
print("Fim")'''

'''r = "s"

while r == "s":
  r = input("Quer continuar? s/n: ".strip().lower())
print("Fim")'''

n = 1

par = impar = 0

while n != 0:
  n = int(input("Digite um numero: "))
  if n % 2 == 0:
    par += 1
  else:
    impar += 1
print(f"""Par: {par}
Ímpar: {impar}""")
print("Fim")