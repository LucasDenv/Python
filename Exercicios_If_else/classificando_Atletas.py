# # A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade :
from datetime import date

nome = input('Nome: ')
ano_atual = date.today().year
ano_nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('{} tem {} anos e se classifica como Atleta MIRIM'.format(nome,idade))

elif idade <= 14:
    print('{} tem {} anos e se classifica como Atleta INFANTIL'.format(nome,idade))

elif idade <= 19:
    print('{} tem {} anos e se classifica como Atleta JUNIOR'.format(nome,idade))

elif  idade <= 25:
    print('{} tem {} anos e se classifica como Atleta SENIOR'.format(nome,idade))

elif idade > 25:    # # Poderia ter utilizado apenas um ELSE, mas visando um codigo limpo é bom usar elif com um argumento, dando uma noçao do sentido 
    print('{} tem {} anos e se classifica como Atleta MASTER'.format(nome,idade))



