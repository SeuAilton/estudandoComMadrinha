# DESAFIO 101
# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
# nas eleições.

def voto(ano):
  from datetime import date
  ano_atual = date.today().year
  idade = ano_atual - ano
  if idade < 16:
    return f"Com {idade} anos: VOTO NEGADO"
  if idade >= 16:
    if idade < 18 or idade > 70:
      return f"Com {idade} anos: VOTO OPCIONAL"
  return f"Com {idade} anos: VOTO OBRIGATÓRIO"


ano_de_nascimento = int(input("Em que ano você nasceu? ").strip())
print(voto(ano_de_nascimento))

