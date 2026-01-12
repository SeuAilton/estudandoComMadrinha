# DESAFIO 085
# Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores
# pares e ímpares em ordem crescente.

lista = list()
par = list()
impar = list()

for n in range(0, 7):
  numero = int(input("Número: ").strip())
  if numero % 2 == 0:
    par.append(numero)
  else:
    impar.append(numero)

lista.append(par[:])
lista.append(impar[:])
lista[0].sort()
lista[1].sort()

print(f"Números pares: {lista[0]}")
print(f"Número ímpares: {lista[1]}")

