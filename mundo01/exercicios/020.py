#DESAFIO 020
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno01 = input("Primeiro aluno: ")
aluno02 = input("Segundo aluno: ")
aluno03 = input("Terceiro aluno: ")
aluno04 = input("Quarto aluno: ")
lista_de_alunos = [aluno01, aluno02, aluno03, aluno04]
random.shuffle(lista_de_alunos)
print(f"Lista de alunos: {lista_de_alunos}")
