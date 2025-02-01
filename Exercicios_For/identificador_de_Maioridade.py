# # programa que compara 7 pessoas e diz as que nao atigiram maioridade (21 anos) 
from datetime import date
ano_atual = date.today().year
list_nome = []    
list_idade = []
list_maioridade = []
list_menoridade = []
for qtd in range (0,7):
    print('\nRegistro da pessoa numero {}\n'.format(qtd+1))
    nome = str(input('Nome: '))
    ano_nasc = int(input('Ano de nascimento: '))
    list_nome.append(nome)
    idade = ano_atual - ano_nasc
    list_idade.append(idade)

    if idade >= 21:
       list_maioridade.append(qtd)
    else:
       list_menoridade.append(qtd)

quantidade = len(list_maioridade)
print('\n As {} Pessoas que atingiram a maioridade\n'.format(quantidade))
for aux in list_maioridade:
    print('{}, {} anos\n'.format(list_nome[aux], list_idade[aux]))

quantidade = len(list_menoridade)
print('\n As {} Pessoas que são a menoridade\n'.format(quantidade))
for aux in list_menoridade:
    print('{}, {} anos\n'.format(list_nome[aux], list_idade[aux]))

print(list_nome)
print(list_idade)
