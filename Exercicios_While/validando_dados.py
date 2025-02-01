     # # Faça um progrma que leia  o SEXO de uma pessoa, mas só aceite 'M' ou 'F'. Caso esteja errado, peça a digitação novamente ate ter uma resposta valida.
     # Pergunte o sexo da pessoa
     # Uma estrutura de  repetiçao que repita a pergunta ate uma resposta valida

from time import sleep
import os

sexo = str(input("Informe seu Sexo: [M/F] ")).strip().upper()[0]
while sexo not in 'MmFf':
    print("Erro: Sexo não reconhecido !!!")
    sleep(2)
    os.system("cls")
    sexo = str(input("Informe seu Sexo: [M/F] ")).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))



