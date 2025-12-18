# DESAFIO 062
#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0(zero) termos.

termo = int(input("Termo: ").strip())
razao = int(input("Razão: ").strip())

n = 0
t = 10

while n < t:
  trem = termo + razao * n
  n += 1
  print(trem)
  if n >= t:
    resposta = int(input("Deseja mostrar mais quantos termos [digite 0(zero) para terminar]? ").strip())
    if resposta != 0:
      t += resposta
    else:
      n = t

