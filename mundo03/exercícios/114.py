# DESAFIO 114
# Crie um código em Python que teste se o site Pudim está acessível
# pelo computador usado.
import requests

def estaNoAr(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.HTTPError as http_error:
    print("\033[0;31mSite não encontrado.\033[m")
    print(f"\033[0;31mERRO HTTP: {http_error}[m")
  except requests.Timeout as time_err:
    print("\033[0;31mNão foi possível conectar ao site.\033[m")
    print(f"\033[0;31mERRO Timeout: {time_err}[m")
  except requests.RequestException as error:
    print("\033[0;31mSite não encontrado.\033[m")
    print(f"\033[0;31mERRO: {error}\033[m")
  else:
    print("\033[0;32mSucesso! O site está no ar.\033[m")


estaNoAr("https://pudim.com.br/")
estaNoAr("https://madrinha.com.br")

