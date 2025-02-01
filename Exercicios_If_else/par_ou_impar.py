## Crie um programa que leia um número inteiro e mostre na tela se é par ou impa
n = int(input("Digite um número para verificarmos se é par ou impar: "))
if(n % 2 == 0):
  print("{} é um número par".format(n))

else:
  print("{} é um número impar".format(n))
