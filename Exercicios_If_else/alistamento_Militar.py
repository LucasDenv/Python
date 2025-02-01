# # Alistamento
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))  
idade= ano_atual - ano_nascimento

if idade > 18 :
    saldo = idade - 18  
    print('''Ja passou o tempo de se alistar
voce deveria ter se alistado ha {} anos.'''.format(saldo))
    ano = ano_atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))

elif idade < 18 :
    saldo = 18 - idade
    ano = ano_atual + saldo
    print("Ainda irá se alistar")
    print("Falta {} anos para se alistar".format(18 - (ano_atual - ano_nascimento)))
    print('Seu alistamento sera em {} .'.format(ano))

else: 
    print("Hora de se Alistar")
