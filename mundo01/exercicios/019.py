#DESAFIO 019
#Um professor quer sortear um do seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno01 = input("Primeiro aluno: ")
aluno02 = input("Segundo aluno: ")
aluno03 = input("Terceiro aluno: ")
aluno04 = input("Quarto aluno: ")
lista_de_alunos = [aluno01, aluno02, aluno03, aluno04]
aluno_aleatorio = random.choice(lista_de_alunos)
print(f"O aluno escolhido foi: {aluno_aleatorio}")
