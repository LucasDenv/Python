    ## Faça um programa que pergunte ao usuario qual a tabuada ele deseja e que só pare de perguntar a tabuada desejada quando o usuario pedir a tabuada de um numero negativo
def multiplicar (number_a, number_b):
    return number_a*number_b
number = 0

while True: 
    number = int(input('insira o número da tabuda desejada: '))
    if number<0:
        break
    for aux in range (1,11):
        print(f'{number} x {aux} = {multiplicar(number,aux)}')

