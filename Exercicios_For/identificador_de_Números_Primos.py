# # Verificador de numero primos

# # primeiro verificamos o conjuto de possibilidade que nao o fariam ser  primos
# não pode  ser (1,2,3,5,7)
# não pode ser divisivel por 2(tira os numeros pares), nao pode ser divisivel por: 2,3,5,7 e sobrar zero

print('{:=^40}'.format(' Verificador de numero primos '))
number = int(input('Digite um numero: '))

if(number != 1 and number != 2 and number !=3 and number !=5 and number !=7 ):
    if(number %2 != 0 and number %3 != 0 and number %5 != 0 and number %7 != 0 ):
        print('{} é primo'.format(number))
    else:
        print('{} NÃO é primo'.format(number))
else:
    print('{} é primo'.format(number))
 