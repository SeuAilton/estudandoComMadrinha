n = 0
s = 0

while True:
  n = int(input("Digite um número: ").strip())
  if n == 999:
    break
  s += n

print(f"A soma dos números é: {s}")
