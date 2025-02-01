# # Ler 6 numeros inteiros e mostre a  soma apenas dos  que forem pares , se o valor for impar desconsidere-o
soma = 0
for aux in range(0,6):
    number = int(input("Digite um numero: "))
    if number %2 == 0 :
        soma += number
print(soma)