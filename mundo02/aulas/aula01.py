nome = input("Qual seu nome? ").strip().capitalize()

if nome == "Preludio":
  print("Nome bunito sô.")
elif nome == "Madrinha" or nome == "Moka" or nome == "Jubs":
  print("Nome bunitin também em.")
elif nome in "Lemos Mina Lexi":
  print("Belo nome moça.")
else:
  print("Nome feio do caramba. Melhore!")
print(f"Bão dia {nome}!")

