#DESAFIO 042
#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: todos os lados iguais
#- Isóceles: dois lados iguais
#- Escaleno: todos os lados diferentes

reta01 = int(input("Primeira reta: ").strip())
reta02 = int(input("Segunda reta: ").strip())
reta03 = int(input("Terceira reta: ").strip())
lista = [reta01, reta02, reta03]
ordenando = lista.sort()
resultado = lista[0] + lista[1]
if resultado > lista[-1]:
  print("É possível fazer um triângulo ", end="")
  if reta01 == reta02 == reta03:
    print("equilátero.")
  elif reta01 != reta02 != reta03 != reta01:
    print("escaleno.")
  else:
    print("isóceles.")
else:
  print("Não é possível fazer um trinângulo")

