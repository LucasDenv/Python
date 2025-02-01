# # Some os numeros IMPARES multiplos de 3 que estao entre 1 ate 500
soma = 0
contador = 0
for number in range (1, 500+1, 2): ## conta so os numeros impares
    if number % 3 == 0:
        contador += 1
        soma += number
    
print('A soma de todos os {} numeros impares multiplos de 3 que estao entre 1 ate 500 é {} e '.format(contador,soma))
