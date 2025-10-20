import math
import random
from playsound3 import playsound
import multiprocessing

#DESAFIO 016
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#    O número 6.127 tem a parte inteira 6.
'''
n1 = float(input("Número Real: "))
conversao = int(n1)
print(f"O número {n1} tem a parte inteira {conversao}.")

'''

#DESAFIO 017
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
cateto_oposto = int(input("Cateto oposto: "))
cateto_adjacente = int(input("Cateto adjacente: "))
hipotenusa = (pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
raiz = math.sqrt(hipotenusa)
print(f"Hipotenusa: {raiz}")

'''

#DESAFIO 018
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
angulo = float(input("Ângulo: "))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print(f"Seno: {seno:.2f} \nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")

'''

#DESAFIO 019
#Um professor quer sortear um do seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
aluno01 = input("Primeiro aluno: ")
aluno02 = input("Segundo aluno: ")
aluno03 = input("Terceiro aluno: ")
aluno04 = input("Quarto aluno: ")
lista_de_alunos = [aluno01, aluno02, aluno03, aluno04]
aluno_aleatorio = random.choice(lista_de_alunos)
print(f"O aluno escolhido foi: {aluno_aleatorio}")

'''

#DESAFIO 020
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
aluno01 = input("Primeiro aluno: ")
aluno02 = input("Segundo aluno: ")
aluno03 = input("Terceiro aluno: ")
aluno04 = input("Quarto aluno: ")
lista_de_alunos = [aluno01, aluno02, aluno03, aluno04]
sorteados = sorted(lista_de_alunos)
print(f"Lista de alunos: {sorteados}")

'''

#DESAFIO 021
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
play = multiprocessing.Process(target=playsound, args=("/home/ailton/Downloads/Wind.mp3",))
play.start()
input("Enter pra parar")
play.terminate()
'''
