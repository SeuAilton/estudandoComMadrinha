# DESAFIO 093
# Crie um programa que gerencie o aproveitamento de um jogador de
# futebol. O programa vai ler o nome do jogador e quantas partidas ele
# jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total
# de gols feitos durante o campeonato.

aproveitamento = {}
todos_os_gols = []

jogador = input("Nome do jogador: ").strip().capitalize()
partidas = int(input("Quantidade de partidas: ").strip())
total_gols = 0
aproveitamento["jogador"] = jogador
aproveitamento["partidas"] = partidas
for g in range(partidas):
  gols = int(input(f"Gols feitos no {g+1}° jogo: ").strip())
  todos_os_gols.append(gols)
  total_gols += gols
aproveitamento["gols"] = todos_os_gols 
aproveitamento["total_gols"] = total_gols

print(f"Jogador{aproveitamento["jogador"]:.>15}")
print(f"Partidas{aproveitamento["partidas"]:.>14}")
print(f"Gols: {aproveitamento["gols"]}")

