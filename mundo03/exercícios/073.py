# DESAFIO 073
# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Vasco.

tabela = ("Flamengo", "Palmeiras", "Cruzeiro", 
          "Mirasol", "Fluminense", "Botafogo", 
          "Bahia", "São Paulo", "Grêmio", 
          "RB Bragantino", "Atlético-MG", "Santos", 
          "Corinthians", "Vasco", "Vitória", 
          "Internacional", "Ceará", "Fortaleza", 
          "Juventude", "Sport")

top5 = tabela[0:5]
bottom4 = tabela[-4:]
alfabetica = sorted(tabela)
posicao = tabela.index("Vasco")

print(f"""Top 5 do Campeonato Brasileiro: {top5}
Últimos 4 do Campeonato Brasileiro: {bottom4}
Todos os times em ordem alfabética: {alfabetica}
Posição do Vasco no campeonato: {posicao}""")

