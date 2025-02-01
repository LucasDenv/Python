# # Calculo de IMC
print('Preencha as informacoes solicitadas abaixo.')
nome = input('Nome: ')
altura = float(input('Altura(m): '))
peso = float(input('Peso(Kg): '))
calculo_Imc = peso/(altura)**2

if calculo_Imc < 18.5:
    print('{} voce esta Abaixo do Peso com o IMC de {:.2f}'.format(nome,calculo_Imc))

elif 18.5 <= calculo_Imc < 25:
    print('{} voce esta com o Peso Ideal com o IMC de {:.2f}'.format(nome,calculo_Imc))

elif 25 <= calculo_Imc < 30:
    print('{} voce esta com Sobrepeso com o IMC de {:.2f}'.format(nome,calculo_Imc))

elif 30 <= calculo_Imc < 40:
    print('{} voce esta com Obesidade com o IMC de {:.2f}'.format(nome,calculo_Imc))

else:
    print('{} voce esta com Obesidade Mórbida com o IMC de {:.2f}'.format(nome,calculo_Imc))

