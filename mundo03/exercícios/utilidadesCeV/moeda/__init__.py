def moeda(n):
  return f"R${n:.2f}"


def metade(n, formatado=False):
  if formatado:
    return moeda(n / 2)
  return n / 2


def dobro(n, formatado=False):
  if formatado:
    return moeda(n * 2)
  return n * 2


def aumento(n, per=0, formatado=False):
  if formatado:
    return moeda(n + (per / 100) * n)
  return n + (per / 100) * n


def reduzir(n, per=0, formatado=False):
  if formatado:
    return moeda(n - (per / 100) * n)
  return n - (per / 100) * n


def titulo(msg):
  tam = len(msg) + 14
  return f"""{'-' * tam}
       {msg}       
{'-' * tam}
"""


def resumo(n, a, r):
  return print(f"""{titulo("RESUMO DO VALOR")}
Preço analizado:  {moeda(n).replace('.', ',')}
Dobro do preço:   {dobro(n, True).replace('.', ',')}
Metade do preço:  {metade(n, True).replace('.', ',')}
{a}% de aumento:   {aumento(n, a, True).replace('.', ',')}
{r}% de redução:   {reduzir(n, r, True).replace('.', ',')}
{'-' * 29}
"""
)


