# Operadores Aritiméticos 

'''
 +  = adição
 -  = subtração
 *  = multiplicação
 /  = divisão
 ** = potência
 // = divisão inteira
 %  = resto da divisão
'''

'''
print(5 + 2)  # 5 + 2  == 7
print(5 - 2)  # 5 - 2  == 3
print(5 * 2)  # 5 * 2  == 10
print(5 / 2)  # 5 / 2  == 2.5
print(5 ** 2) # 5 ** 2 == 25
print(5 // 2) # 5 // 2 == 2
print(5 % 2)  # 5 % 2  == 1
print("-" * 50)
'''

'''
Ordem de Precedência 

1 - ()
2 - **
3 - *, /, //, %
4 - +, -

'''

#Exemplos

'''
print(5 + 3 * 2)        # == 11
print(5 * 3 + 4 ** 2)   # == 31
print(3 * (5 + 4) ** 2) # == 243

print("-" * 50)
'''
'''
nome = input("Nome: ")
print(f"Nome {nome:20}!")
print(f"Nome {nome:>20}!")
print(f"Nome {nome:=>20}!")
print(f"Nome {nome:^20}!")
print(f"Nome {nome:=^20}!".upper())
print(f"Nome {nome:=^20}!".lower())
'''

n1 = int(input("Número01: "))
n2 = int(input("Número02: "))
d = n1 / n2
print(f"Resultado {d:.2f}", end=" ") 
# (:.2f) = formata casas decimais 
# (end="") = junta os prints
print("Junta tudo garai")
print("agora \n eu quero quebrar \n os trem tudo \n sô")
# (\n) = quebra de linha

#terminamos Curso Python #07 - Operadores Aritméticos