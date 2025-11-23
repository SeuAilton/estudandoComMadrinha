#DESAFIO 027
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ùltimo nome separadamente.
#Ex: Ana Maria de Souza
#    primeiro: Ana
#    segundo: Souza

nome = input("Nome: ").strip()
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]
print(primeiro_nome)
print(ultimo_nome)
