from random import randint

## Computador pensa em um numero inteiro de 0 a 5 

n_escolhido_pc = randint(0,5)

## computador pede para o usuario tentar descobrir qual foi o numero escolhido pelo computador
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar..')
print('-=-' * 20)
n_usuario = int(input('Em que número eu pensei ? '))

## Programa  deve avisar se o usuario acertou ou errou   
if(n_escolhido_pc == n_usuario):
  print("Você acertou o número escolhido pelo pc !!!")
else:
  print("você Errrou")
  print("O numero era {}".format(n_escolhido_pc))

