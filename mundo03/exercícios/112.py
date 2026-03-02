# DESAFIO 112
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função input(), mas com a validação de dados para aceitar
# apenas valores que sejam monetários.
from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro("Digite um valor: R$")
moeda.resumo(p, 35, 22)

