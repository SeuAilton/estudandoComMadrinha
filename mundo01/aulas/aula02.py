#Tipos Primitivos
'''
nada = None #None
print(nada)

numero = 0 #Number
print(numero)

texto = "zero" #String
print(texto)

verdadeiro_ou_falso = True #Boleam
print(verdadeiro_ou_falso)

numero_real = 5.0 #Float
print(numero_real)
'''

'''
n1 = input("Número 01: ")
print(type(n1))

n2 = int(input("Número 02: "))
print(type(n2))
'''

'''
n1 = int(input("Número 01: "))
n2 = int(input("Número 02: "))
soma = n1 + n2
print(f"A soma entre {n1} e {n2} vale {soma}")
'''

n1 = input("Número: ")
print(n1.isnumeric())

n2 = input("Letra: ")
print(n2.isalpha())

n2 = input("Alfanumérico: ")
print(n2.isalnum())