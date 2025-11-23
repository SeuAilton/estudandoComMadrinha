#DESAFIO 049
#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Número:").strip())
multiplicado = 0

for c in range(1, 11):
  multiplicado += 1
  print(f"{numero} x {multiplicado:2} = {c * numero}")
