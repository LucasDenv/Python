        #  # Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas. No final do program mostre .
        # A Media de idade do Grupo.
        # Qual é o nome do homem mais velho .
        # Quantas mulheres tem menos de 20 anos.

# desenvolver 3 arrays  que guarde cada tipo e cada pessoa vira uma indice ID.
# um for que registre 3 caracteristicas de cada umad as 4 pessoas. 

list_Nome = []
list_Idade = []
list_Sexo = []

for aux in range(1,6):
    print('-=-' * 7)
    print('Cadastro Pessoa N{}'.format(aux))
    print('-=-' * 7)
    list_Nome.append(str(input("\nNome(Pessoa {}): ".format(aux)))) 
    list_Idade.append(int(input("\nIdade(Pessoa {}): ".format(aux))))
    list_Sexo.append(str(input("\nSexo(Pessoa {}): ".format(aux))))
# A Media de idade do Grupo.
media = sum(list_Idade) / len(list_Idade)
print("A media das idades é {}".format(media))
# Qual é o nome do homem mais velho .
homem_mais_velho = ''
idade_homem_velho = 0

for i in range(5):
    if list_Sexo[i] == "M" and list_Idade[i] > idade_homem_velho:
        idade_homem_velho = list_Idade[i]
        homem_mais_velho = list_Nome[i]
if homem_mais_velho !=0:
    print('O homem mais velho é: {} com {} anos.'.format(homem_mais_velho,idade_homem_velho))
else:
    print('Não há homens no grupo.')


# Quantas e quais mulheres tem menos de 20 anos.
qtd_mulheres_menos20 = 0
nome_mulheres_menos20 = []
idade_mulheres_menos20 = []

for i in range(5):
    if list_Sexo[i] == 'F' and list_Idade[i] < 20:
        qtd_mulheres_menos20 += 1
        nome_mulheres_menos20.append(list_Nome[i])
        idade_mulheres_menos20.append(list_Idade[i])
if qtd_mulheres_menos20 != 0:
    print('Há {} mulheres com menosde 20 anos, nome delas: {} e idade delas em ordem: {}'.format(qtd_mulheres_menos20,nome_mulheres_menos20,idade_mulheres_menos20))

