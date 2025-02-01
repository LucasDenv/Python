     ## O jogo irá escolher um número de 0 a 100 e o jogador tera no maximo 7 chances para descobri o numero escolhido, apos cada palpite o sistema o informara se ele palpitou um numero mais alto ou mais baixo do que o pensado (isso funciona pra demonstrar a importancia de uma estrutura de codigo chamada arvore, pq com dados armazenados em uma arvore binaria , voce leva no maximo 7 chances para achar o dado procurado em um montante com 128 dados)

from  random import randint

n_sorteado = int(randint(0,100))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 100. Tente advinhar em no maximo 7 tentativas ...')
print('-=-' * 20)

palpite = int(input('Em que número eu pensei ? '))
tentativas = 0
tentativas += 1
if tentativas !=7:
    while tentativas!=7 and palpite != n_sorteado :
        if palpite > n_sorteado:
            print('O numero o qual voce palpitou é MAIOR que o numero pensado !!! tente novamente')
        else: 
            print('O numero o qual voce palpitou é MENOR que o numero pensado !!! tente novamente')
        palpite = int(input('Em que número eu pensei ? '))
        tentativas += 1
if palpite == n_sorteado:
    print('Parabens !!! Voce acertou o numero escolhido foi {} e voce levou {} tentativas para acertar'.format(n_sorteado, tentativas))
else:
    print('Voce esgotou suas tentativas !!! O numero pensado foi {}'.format(n_sorteado))

 

