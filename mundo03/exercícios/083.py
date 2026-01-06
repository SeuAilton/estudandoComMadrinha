# DESAFIO 083
# Crie um programa onde o usuário digite uma explressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a 
# expressão passada está com os parênteses abertos e fechados na
# ordem correta.

ex = input("Expressão: ").strip().replace(" ", "")
lista = list(ex)
c = 0

for v in lista:
  if v == "(":
    c += 1
  elif v == ")":
    c -= 1

if c == 0:
  print(f"A expressão {ex} está correta.")
else:
  print(f"A expressão {ex} está errada.")
    
