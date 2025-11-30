#Desafio 056
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#-> A média de idade do grupo
#-> Qual é o nome do homem mais velho.
#-> Quantas mulheres tem menos de 20 anos.

maiscabado = 0
nome_maiscabado = ""
mais_novinha = ""
soma = 0
mulheres = 0

for i in range(4):
  print(f"------ {i+1}ª pessoa ------")
  nome = input("Nome: ").strip().title()
  idade = int(input("Idade: ").strip())
  sexo = input("Sexo [M/F]: ").strip().lower()

  soma += idade

  if i == 0 and sexo == "m":
    maiscabado = idade
    nome_maiscabado = nome
  if idade > maiscabado and sexo == "m":
    maiscabado = idade
    nome_maiscabado = nome
  if sexo == "f" and idade < 20:
    mulheres += 1
    mais_novinha = nome

media = soma / 4

print(f"""Média de idade do grupo: {media:.1f}
O Homem mais velho é: {nome_maiscabado}
Mulheres com menos de 20 anos: {mulheres}
Mulher mais nova: {mais_novinha}""")
