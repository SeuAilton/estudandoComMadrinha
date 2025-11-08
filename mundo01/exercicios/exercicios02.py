#DESAFIO 05
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''
n1 = int(input("N1: "))
antecessor = n1 - 1
sucessor = n1 + 1
print(f"Antecessor = {antecessor} \nSucessor = {sucessor}")

'''
'''
n1 = int(input("N1: "))
print(f"Antecessor = {n1 - 1} \nSucessor = {n1 + 1}")

'''

#DESAFIO 06
# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
'''
n1 = int(input("N1: "))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** 0.5
print(f"Dobro = {dobro} \nTriplo = {triplo} \nRaiz = {raiz:.2f}")
'''
'''
n1 = int(input("N1: "))
print(f"Dobro = {n1 * 2} \nTriplo = {n1 * 3} \nRaiz = {n1 ** 0.5:.2f}")

'''
'''
n1 = int(input("N1: "))
dobro = n1 * 2
triplo = n1 * 3
raiz = pow(n1 , 0.5)
print(f"Dobro = {dobro} \nTriplo = {triplo} \nRaiz = {raiz:.2f}")

'''

#DESAFIO 07
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

'''
nota01 = float(input("Primeira nota: "))
nota02 = float(input("Segunda nota: "))
media = (nota01 + nota02) / 2
print(f"Média do aluno = {media:.1f}")

'''

#DESAFIO 08
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

'''
valor = float(input("Metros: "))
km = valor / 1000
hm = valor / 100
dan = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print(f"Kilômetros = {km:.1f} \nHectômetro = {hm:.1f} \nDecâmetro = {dan:.1f} \nMetros = {valor:.0f} \nDecímetro = {dm:.0f}dm \nCentímetro = {cm:.0f}cm \nMilímetro = {mm:.0f}mm")

'''

#DESAFIO 09
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

'''
n1 = int(input("Número: "))
vezes2 = n1 * 2
vezes3 = n1 * 3
vezes4 = n1 * 4
vezes5 = n1 * 5
vezes6 = n1 * 6
vezes7 = n1 * 7
vezes8 = n1 * 8
vezes9 = n1 * 9
vezes10 = n1 * 10
'''
'''
print("-" * 20)
print(f"1  x {n1} = {n1} \n2  x {n1} = {vezes2} \n3  x {n1} = {vezes3} \n4  x {n1} = {vezes4} \n5  x {n1} = {vezes5} \n6  x {n1} = {vezes6} \n7  x {n1} = {vezes7} \n8  x {n1} = {vezes8} \n9  x {n1} = {vezes9} \n10 x {n1} = {vezes10}")
print("-" * 20)
'''
'''
print("-" * 20)
print(f"{n1} + {1:2} = {n1}")
print(f"{n1} + {2:2} = {vezes2}")
print(f"{n1} + {3:2} = {vezes3}")
print(f"{n1} + {4:2} = {vezes4}")
print(f"{n1} + {5:2} = {vezes5}")
print(f"{n1} + {6:2} = {vezes6}")
print(f"{n1} + {7:2} = {vezes7}")
print(f"{n1} + {8:2} = {vezes8}")
print(f"{n1} + {9:2} = {vezes9}")
print(f"{n1} + {10:2} = {vezes10}")
print("-" * 20)
'''

#DESAFIO 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$ 1,00 = R$ 3,27

'''
dinheiro = float(input("Dinheiro: R$ "))
conversao = dinheiro / 3.27
conversao_nova = dinheiro / 5.43
print(f"Convertido pra dólar = {conversao:.2f} \nConversão atual = {conversao_nova:.2f}")

'''

#DESAFIO 11
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

'''
largura = float(input("Largura: "))
altura = float(input("Altura: "))
area = largura * altura
pintar = area / 2
print(f"Tinta necessária: {int(pintar)}l")

'''

#DESAFIO 12
# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

'''
preco = float(input("Preço: R$ "))
desconto = preco * (1 - 0.05)
print(f"Novo preço: R$ {desconto:.2f}")

'''

#DESAFIO 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

'''
salario = float(input("Salário: R$ "))
aumento = salario * 1.15
print(f"Novo salário: R$ {aumento:.2f}")

'''
