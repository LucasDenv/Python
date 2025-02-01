# # Programa para aprovarr o emprestimo bancario

# # 1. Perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
valor_Casa = float(input('Qual valor do imóvel a ser financiado? R$ '))
renda_Comprador = float(input('Qual salário do comprador? R$ '))
tempo_Financiamento = int(input('Em quantos anos pretende quitar o imóvel? '))

# # 2. Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
def calculo_Prestacao():
    tempo = tempo_Financiamento * 12
    valor_Prestacao = valor_Casa / tempo
    return valor_Prestacao

prestacao = calculo_Prestacao()

if prestacao <= (renda_Comprador * 30) / 100:
    print('Empréstimo Aprovado! Sua prestação será de R$ {:.2f}'.format(prestacao))
else:
    print('Empréstimo NEGADO! A prestação de R$ {:.2f} excede 30% da sua renda.'.format(prestacao))
