teste = list()
teste.append("Preludio")
teste.append(29)
galera = list()
galera.append(teste[:])
teste[0] = "Madrinha"
teste[1] = 25
galera.append(teste[:])
print(galera)

pessoinha = [["Madrinha", 25], ["Moka", 665], ["Jubs", 32], ["Mina", 29]]
print(pessoinha[1][0])
for p in pessoinha:
  print(f"{p[0]} tem {p[1]} anos.")

galego = list()
dados = list()
total_maior = total_menor = 0
for c in range(0, 3):
  dados.append(input("Nome: ").strip())
  dados.append(int(input("Idade: ").strip()))
  galego.append(dados[:])
  dados.clear()
print(galego)

for p in galego:
  if p[1] >= 18:
    print(f"{p[0]} é maior de idade.")
    total_maior += 1
  else:
    print(f"{p[0]} é menor de idade.")
    total_menor += 1
print(f"""Foram {total_maior} maiores de idade
Foram {total_menor} menores de idade.""")

