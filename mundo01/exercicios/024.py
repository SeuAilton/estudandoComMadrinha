#DESAFIO 024
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Nome da cidade: ").strip()
cidade_maiusculo = cidade.upper()
primeiro_nome_da_cidade = cidade_maiusculo.split()[0]
achando_o_santo = primeiro_nome_da_cidade.find("SANTO")
if achando_o_santo == -1:
  print(f"A cidade {cidade.title()} não começa Santo no nome.")
else:
  print(f"A cidade {cidade.title()} começa Santo no nome.")
