def moeda(n):
  return f"R${n:.2f}".replace('.', ',')


def metade(n=0, formatado=False):
  res = n / 2
  return res if not formatado else moeda(res)


def dobro(n=0, formatado=False):
  res = n * 2
  return res if not formatado else moeda(res)


def aumento(n=0, per=0, formatado=False):
  res = n + (per / 100) * n
  return res if not formatado else moeda(res)


def reduzir(n=0, per=0, formatado=False):
  res = n - (per / 100) * n
  return res if not formatado else moeda(res)


def titulo(msg):
  tam = len(msg) + 14
  return f"""{'-' * tam}
       {msg}       
{'-' * tam}
"""


def resumo(n, a, r):
  return print(f"""{titulo("RESUMO DO VALOR")}
Preço analizado:  {moeda(n)}
Dobro do preço:   {dobro(n, True)}
Metade do preço:  {metade(n, True)}
{a}% de aumento:   {aumento(n, a, True)}
{r}% de redução:   {reduzir(n, r, True)}
{'-' * 29}
"""
)


