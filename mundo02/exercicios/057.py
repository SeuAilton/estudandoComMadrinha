#DESAFIO 057
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ""

while sexo != "M" and sexo != "F":
  sexo = input("Sexo [M/F]: ").strip().upper()[0]
  if sexo != "M" and sexo != "F":
    print('[ERRO]Escreva "M" para masculino ou "F" para feminino!')

if sexo == "M":
  print("Seu sexo é: Masculino")
else:
  print("Seu sexo é: Feminino")

'''
sexo = input("informe seu sexo: [M/F] ").strip().upper()[0]

while sexo not in "MF":
  sexo = input("Dados inválidos. Por favor, informe seu sexo: ").strip().upper()[0]

print(f"Sexo {sexo} registrado com sucesso.")
'''

