# DESAFIO 097
# Faça um programa que tenha uma função chamada escreva(), que recebe
# um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.
# Ex:
# escreva("Olá, Mundo!")
# Saída:
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~

def escreva(texto):
  print("~" * len(texto))
  

trem = input("Texto qualquer: ").strip()

escreva(trem)
print(trem)
escreva(trem)

