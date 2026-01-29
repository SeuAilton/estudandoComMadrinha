# DESAFIO 101
# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
# nas eleições.
from datetime import date

def voto(ano):
  idade = ano_atual - ano
  if idade < 16:
    return "NEGADO"
  if idade >= 16:
    if idade < 18 or idade > 70:
      return "OPCIONAL"
  return "OBRIGATÓRIO"


ano_atual = date.today().year
ano_de_nascimento = int(input("Em que ano você nasceu? ").strip())
idade = ano_atual - ano_de_nascimento

print(f"Com {idade} anos: VOTO {voto(ano_de_nascimento)}.")

