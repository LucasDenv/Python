# # Faca um programa que leia o peso de 5 pessoas. No final mostre qual o maior e o menor peso lido
nome = []
peso = []
maior_peso = 0
menor_peso = 0
auxMaior = 0
auxMenor = 0
for pessoa in range (1,6):
    nome.append(str(input('\nInforme o NOME da pessoa n {}: '.format(pessoa))))
    peso.append(float(input('\nInforme o PESO da pessoa n {}: '.format(pessoa))))
    if pessoa == 1:
        maior_peso = peso[pessoa-1]
        menor_peso = peso[pessoa-1]
    else:
        if peso[pessoa-1] > maior_peso:
            maior_peso = peso[pessoa-1]
            auxMaior = pessoa-1
        if peso[pessoa-1] < menor_peso:
            menor_peso = peso[pessoa-1]
            auxMenor = pessoa-1
print('\nMaior peso lido foi de {}kg da pessoa {}'.format(maior_peso,nome[auxMaior]))
print('\nMenor peso lido foi de {}kg da pessoa {}'.format(menor_peso,nome[auxMenor]))


print(peso)

