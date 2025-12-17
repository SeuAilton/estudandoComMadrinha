#DESAFIO 069
#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

pessoas18 = 0
homi = 0
novinhas = 0

while True:
  while True:
    sexo = input("Qual o seu sexo?[M/F] ").strip().upper()[0]
    if sexo != "F" and sexo != "M":
      print("[ERRO] Digite uma opção válida.")
    else:
      break
  
  idade = int(input("Qual a sua idade? ").strip())

  if idade > 18:
    pessoas18 += 1
  
  if sexo == "F":
    if idade < 20:
      novinhas += 1
  else:
    homi += 1

  continuar = input("Deseja continuar o cadastro?[S/N] ").strip().upper()[0]

  if continuar == "N":
    break

print(f"Pessoas com mais de 18 anos: {pessoas18}.")
print(f"Homens cadastrados no sistema: {homi}.")
print(f"Mulheres cadastradas com menos de 20 anos: {novinhas}.")
