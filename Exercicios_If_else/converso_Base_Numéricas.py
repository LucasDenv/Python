# #  Converte numeros inteiros em Binarios, Octal ou Hexadecimal

numero_inteiro = int(input('Digite um número inteiro: '))
print('Opcao 1: Para conversão para Binário.')
print('Opcao 2: Para conversão para Octal.')
print('Opcao 3: Para conversão para Hexadecimal.')
opcao = int(input('Digite a opcao escolhida: '))

if opcao == 1:
   
    print(f'O número {numero_inteiro} em binário é {bin(numero_inteiro)[2:]}')
elif opcao == 2:
   
    print(f'O número {numero_inteiro} em octal é {oct(numero_inteiro)[2:]}')
else:

    print(f'O número {numero_inteiro} em hexadecimal é {hex(numero_inteiro)[2:].upper()}')


