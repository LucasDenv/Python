# # Boletim

nota_1 = float(input('Digite a primeira Nota: '))
nota_2 = float(input('Digite a Segunda Nota: '))

if(((nota_1+nota_2)/2) >= 7):
    print('Aprovado')
elif(((nota_1+nota_2)/2) < 5):
    print("Reprovado")
else:
    print("Recuperacao")



