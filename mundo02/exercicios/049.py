#DESAFIO 049
#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Número:").strip())
for c in range(1, 11):
  print(f"{numero} x {c:2} = {c * numero}")
