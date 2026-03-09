# DESAFIO 114
# Crie um código em Python que teste se o site Pudim está acessível
# pelo computador usado.
import requests

def estaNoAr(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      print("\033[0;32mSucesso! O site está no ar.\033[m")
  except:
    print("\033[0;31mSite não encontrado.\033[m")


estaNoAr("https://pudim.com.br/")
#estaNoAr("")

