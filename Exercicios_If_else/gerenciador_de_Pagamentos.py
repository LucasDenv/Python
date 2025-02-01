# # Calculadora de Pagamentos

print('{:^40}'.format(" LOJA DO The Raven ")) # # Centralizado em 40 espaços
value = float(input("Valor do Produto: "))

print('''OPCAO DE PAGAMENTOS
OPCAO 1 : A vista dinheiro ou cheque (10% de desconto)
OPCAO 2 : A vista no Cartao (5% de desconto)
OPCAO 3 : Em ate 2x no cartao (Preco Normal)
OPCAO 4 : Em  3x ou mais no cartao (20% de Juros''')

option = int(input('Digite uma opcao: '))

if option == 1:
    new_value = value - (value*10/100)
    print("O valor de RS {:.2f}, sendo pago a vista ou por cheque sai por RS {:.2f}".format(value,new_value))
elif option == 2:
    new_value = value - (value*5/100)
    print("O valor de RS {:.2f}, sendo pago a vista no cartao sai por RS {:.2f}".format(value,new_value))
elif option == 3:
    new_value = value/2 
    print("O valor de RS {:.2f}, sendo pago em ate 2x sai por RS {:.2f} cada parcela".format(value,new_value))
elif option == 4:
    qtd_parcel = int(input('Em quantas vezes ira parcelar a compra ? '))
    new_value = value + (value*20/100)
    parcel = new_value / qtd_parcel
    print("O valor de RS {:.2f}, sendo pago em 3x ou mais sai por RS {:.2f} e  cada parcela sair por RS {:.2f}".format(value,new_value,parcel))
else:
    print("\033[1;31;40m OPCAO INVALIDA de pagamento. Tente novamnete !\033[m")