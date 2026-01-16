# DESAFIO 095
# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

aproveitamento = {}
jogadores = []

while True:
  jogador = input("Nome do jogador: ").strip().capitalize()
  partidas = int(input("Quantidade de partidas: ").strip())
  todos_os_gols = []
  aproveitamento["jogador"] = jogador
  aproveitamento["partidas"] = partidas
  for g in range(partidas):
    gols = int(input(f"Gols feitos no {g+1}° jogo: ").strip())
    todos_os_gols.append(gols)
  total_gols = sum(todos_os_gols)
  aproveitamento["gols"] = todos_os_gols[:]
  aproveitamento["total_gols"] = total_gols
  jogadores.append(aproveitamento.copy())
  aproveitamento.clear()
  todos_os_gols.clear()
  while True:
    continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if continuar not in "SN":
      print("[ERRO]Digite uma opção válida!")
    else:
      break
  if continuar == "N":
    break
  
print("-" * 20)
for k, v in enumerate(jogadores):
  print(f"""{k+1}° jogador:
Nome: {v["jogador"]}
Quantidade de partidas: {v["partidas"]}
Gols por partidas: {v["gols"]}
Total de gols no campeonato: {v["total_gols"]}""")
  print("-" * 20)

while True:
  while True: 
    dados = int(input("Mostrar dados de qual jogador? [N°jogador] ").strip())
    if 0 <= (dados-1) < len(jogadores):
      break
    else:
      print("[ERRO]Jogador não existe!")
  print("-" * 20)
  print(f"Jogador: {jogadores[dados - 1]["jogador"]}")
  for k, v in enumerate(jogadores[dados - 1]["gols"]):
    print(f"{k+1}° jogo: {v} gols")
  print("-" * 20)
  while True:
    mdados = input("Mostrar dados de outro jogador? [S/N]").strip().upper()[0]
    if mdados not in "SN":
      print("[ERRO]Digite uma opção válida!")
    else:
      break
  if mdados == "N":
    break

