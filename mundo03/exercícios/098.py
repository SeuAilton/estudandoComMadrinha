# DESAFIO 098
# Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

def contador(inicio, fim, passo):
  for p in range(inicio, fim, passo):
    print(p, end=" ")
  print()


print("-" * 30)
print("Contagem de 1 até 10 de 1 em 1")
contador(1, 11, 1)
print("-" * 30)
print("Contagem de 10 até 0 de 2 em 2")
contador(10, -1, -2)
print("-" * 30)
print("Personalize a contagem!")
i = int(input("Início: ").strip())
f = int(input("Fim: ").strip())
p = int(input("Passo: "))
print("-" * 30)

if f < 0:
  p = -p
  f = f-1 
else:
  f = f+1

if p == 0:
  if f < 0:
    p = -1
  else:
    p = 1

print(f"Contagem personalizada")
contador(i, f, p)
print("-" * 30)

