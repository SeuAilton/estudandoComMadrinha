# DESAFIO 095
# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

aproveitamento = {}
total_gols = 0
jogadores = []

while True:
  jogador = input("Nome do jogador: ").strip().capitalize()
  partidas = int(input("Quantidade de partidas: ").strip())
  aproveitamento["jogador"] = jogador
  aproveitamento["partidas"] = partidas

  for g in range(partidas):
    gols = int(input(f"Gols feitos no {g+1}° jogo: ").strip())
    total_gols += gols
 
  aproveitamento["gols"] = total_gols
  jogadores.append(aproveitamento.copy())
  aproveitamento.clear()

print(f"Jogador{aproveitamento["jogador"]:.>15}")
print(f"Partidas{aproveitamento["partidas"]:.>14}")
print(f"Gols{aproveitamento["gols"]:.>18}")

