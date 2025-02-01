# # Crie um programa que leia varios numero inteiros pelo teclado. O programa que pare quando o usuario digita 999, mostre quantos numeros foi digitado e a soma deles/
number = 0 
count = 0
soma = 0 
while True:
    number = int(input("Digite um número: "))
    if number == 999:
        break
    soma += number
    count += 1 
print(f'voce digitou {count} e a soma deles é {soma}')



