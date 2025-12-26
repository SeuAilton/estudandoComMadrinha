# DESAFIO 072
# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado 
# (entre 0 e 20) e mostra-lo por extenso.

tupla = ("zero", "um", "dois", "três", "quatro", 
         "cinco", "seis", "sete", "oito", 
         "nove", "dez", "onze", "doze", 
         "treze", "quatorze", "quinze", "dezesseis", 
         "dezessete", "dezoito", "dezenove", "vinte")

while True:
  n = int(input("Digite um número entre 0 e 20: ").strip())
  if n < 0 or n > 20:
    print("[ERRO]Digite um número válido!")
  else:
    break

indice = tupla[n]
print(f"O número {n} por extenso é: {indice}")

