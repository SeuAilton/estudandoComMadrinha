# DESAFIO 092
# Crie um programa que leia nome, ano de nascimento e carteira de 
# trabalho e cadastre-os(com idade) em um dicionário se por acaso 
# o CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com
# quantos anos a pessoa vai se aposentar(35anos).
from datetime import date

ano = date.today().year

cadastro = {}

nome = input("Nome: ").strip().capitalize()
nascimento = int(input("Ano de Nascimento: ").strip())
idade = ano - nascimento
ctps = int(input("Número CTPS [0 se não tem]: ").strip())

cadastro["nome"] = nome
cadastro["idade"] = idade

if ctps != 0:
  cadastro["ctps"] = ctps
  contrato = int(input("Ano de contratação: ").strip())
  salario = float(input("Salário: R$").strip())
  aposentadoria = contrato + 35 - nascimento
  cadastro["contrato"] = contrato
  cadastro["salario"] = salario
  cadastro["aposentadoria"] = aposentadoria
  for k,v in cadastro.items():
    print(f"{k}: {v}")
else:
  print(f"""nome: {cadastro["nome"]}
idade: {cadastro["idade"]}""")

