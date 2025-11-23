#DESAFIO 026
#Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

frase = input("Escreve um trem ai: ").strip()
frase_minusculo = frase.lower()
quantos_a = frase_minusculo.count("a")
primeira_aparicao = frase_minusculo.find("a")
ultima_aparicao = frase_minusculo.rfind("a")
print(quantos_a)
print(primeira_aparicao)
print(ultima_aparicao)
