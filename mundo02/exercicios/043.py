#DESAFIO 043
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do Peso
#- Entre 18.5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade mórbida

peso = float(input("Peso: ").strip())
altura = float(input("Altura: ").strip())
imc = peso / (altura * altura)

if imc < 18.5:
  print(f"Seu IMC: {imc:.1f} Abaixo do peso")
elif 18.5 <= imc < 25:
  print(f"Seu IMC: {imc:.1f} Peso ideal")
elif 25 <= imc < 30:
  print(f"Seu IMC: {imc:.1f} Sobrepeso")
elif 30 <= imc < 40:
  print(f"Seu IMC: {imc:.1f} Obesidade")
else:
  print(f"Seu IMC {imc:.1f} Obesidade mórbida")

