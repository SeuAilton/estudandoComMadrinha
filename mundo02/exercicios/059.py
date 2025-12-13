#DESAFIO 059
#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

opcao = None

n1 = int(input("Primeiro valor: ").strip())
n2 = int(input("Segundo valor: ").strip())

while opcao != 5:
  opcao = int(input("[1] para somar\n[2] para multiplicar\n[3] para o maior número\n[4] novos números\n[5] sair do programa\nOpção selecionada: "))
  if opcao == 1:
    print("-=-" *12)
    print(f"A soma entre {n1} e {n2} é: {n1 + n2}")
    print("-=-" *12)
  elif opcao == 2:
    print("-=-" *12)
    print(f"O número {n1} multiplicado por {n2} é: {n1 * n2}")
    print("-=-" *12)
  elif opcao == 3:
    print("-=-" *12)
    print(f"O maior número entre {n1} e {n2} é: {max(n1, n2)}")
    print("-=-" *12)
  elif opcao == 4:
    n1 = int(input("Primeiro valor: ").strip())
    n2 = int(input("Segundo valor: ").strip())
  elif opcao == 5:
    print("Saindo do programa...")
  else:
    print("[ERRO] Opção inválida!")

