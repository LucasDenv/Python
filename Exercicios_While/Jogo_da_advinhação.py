     ## Crie um jogo onde o computador pensa em um numero entre 0 e 10. O jogador tenta advinhar ate acertar o numero e quando ele acertar informe quanto palpites foi necessario.
        # cria um N_sorteado e em seguida solicitar que o jogador palpite um numero
        # um verificador se o numero esta correto
        # criar um cont

from  random import randint

n_sorteado = int(randint(0,10))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar..')
print('-=-' * 20)

palpite = int(input('Em que número eu pensei ? '))
count = 0
count += 1

if palpite != n_sorteado:
    while palpite != n_sorteado:
        print('Não foi esse o numero pensado, tente novamente')
        palpite = int(input('Em que número eu pensei ? '))
        count += 1 

print('Parabens !!! Voce acertou o numero escolhido foi {} e voce levou {} tentativas para acertar'.format(n_sorteado, count))



