# DESAFIO 107
# Crie um módulo chamdo moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

p = float(input("Digite um preço: R$"))
print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumentando em 10%, temo {moeda.aumento(p, 10)}")
print(f"Reduzindo em 13%, temos {moeda.reduzir(p, 13)}")

