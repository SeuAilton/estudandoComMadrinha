#DESAFIO 022
#Crie um programa que leia o nome complero de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas as letas minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.
'''
nome = input("None: ")
maiusculo = nome.upper()
minusculo = nome.lower()
separando_o_nome = nome.split()
tirando_os_espacos = "".join(separando_o_nome)
calculando_quantas_letras = len(tirando_os_espacos)
pegando_o_primeiro_nome = nome.split()[0]
quantas_letras_primeiro_nome = len(pegando_o_primeiro_nome)
print(maiusculo)
print(minusculo)
print(calculando_quantas_letras)
print(quantas_letras_primeiro_nome)

'''

#DESAFIO 023
#Faça um programa que leio um número de 0 a 9999 e mostre no tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#    unidade: 4
#    dezena: 3
#    centena: 8
#    milhar: 1
'''
numero = int(input("Número: "))

if numero > 0 and numero <= 9999:
  unidade = numero % 10
  dezena = (numero - unidade) / 10 % 10
  centena = (numero - dezena) / 100 % 10
  milhar = (numero - centena) / 1000 % 10
  print(unidade)
  print(int(dezena))
  print(int(centena))
  print(int(milhar))
else:
  print("[ERROR]Digite um número entre 0 e 9999!")

'''
#DESAFIO 024
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''
cidade = input("Nome da cidade: ")
cidade_maiusculo = cidade.upper()
primeiro_nome_da_cidade = cidade_maiusculo.split()[0]
achando_o_santo = primeiro_nome_da_cidade.find("SANTO")
if achando_o_santo == -1:
  print(f"A cidade {cidade} não começa Santo no nome.")
else:
  print(f"A cidade {cidade} começa Santo no nome.")

'''

#DESAFIO 025
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
nome = input("Nome: ")
nome_maiusculo = nome.upper()
achando_o_silva = nome_maiusculo.find("SILVA")
if achando_o_silva == -1:
  print(f"O nome {nome} não tem Silva.")
else:
  print(f"O nome {nome} tem Silva.")

'''

#DESAFIO 026
#Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.
'''
frase = input("Escreve um trem ai: ")
frase_minusculo = frase.lower()
quantos_a = frase_minusculo.count("a")
primeira_aparicao = frase_minusculo.find("a")
ultima_aparicao = frase_minusculo.rfind("a")
print(quantos_a)
print(primeira_aparicao)
print(ultima_aparicao)

'''

#DESAFIO 027
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ùltimo nome separadamente.
#Ex: Ana Maria de Souza
#    primeiro: Ana
#    segundo: Souza
'''
nome = input("Nome: ")
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]
print(primeiro_nome)
print(ultimo_nome)

'''