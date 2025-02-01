# # Pedra, Papel e Tesoura
from random import randint
from time import sleep
# # 1 Pedra. 
# # 2 Papel. 
# # 3 Tesoura.
choice_Pc = randint(1,3)
choice_People = input("Pedra, Papel ou Tesoura ? ")

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

# # tratando escolha pessoa
if choice_People == "Pedra":
    choice_People = 1
elif choice_People == "Papel":
    choice_People = 2
elif choice_People == "Tesoura":
    choice_People = 3    

# # Jogo
if (choice_People == 1 and choice_Pc == 3) or (choice_People == 2 and choice_Pc == 1) or (choice_People == 3 and choice_Pc == 2):
    # # tratando escolha pessoa
    if choice_People == 1:
        choice_People = "Pedra"
    elif choice_People == 2:
        choice_People = "Papel"
    elif choice_People == 3:
        choice_People ="Tesoura"  
    # # Tratamento esolha pc 
    if choice_Pc == 1:
        choice_Pc = "Pedra"
    elif choice_Pc == 2:
        choice_Pc = "Papel"
    elif choice_Pc == 3:
        choice_Pc ="Tesoura" 
    print('-='*35)
    print("A escolha do PC foi {} e a sua foi {}, logo voce ganhou !!!".format(choice_Pc,choice_People))
    print('jOGADOR VENCEU')
    print('-='*35)
elif(choice_People == 3 and choice_Pc == 1) or (choice_People == 1 and choice_Pc == 2) or (choice_People == 2 and choice_Pc == 3):
    # # tratando escolha pessoa
    if choice_People == 1:
        choice_People = "Pedra"
    elif choice_People == 2:
        choice_People = "Papel"
    elif choice_People == 3:
        choice_People ="Tesoura"  
    # # Tratamento esolha pc 
    if choice_Pc == 1:
        choice_Pc = "Pedra"
    elif choice_Pc == 2:
        choice_Pc = "Papel"
    elif choice_Pc == 3:
        choice_Pc ="Tesoura" 
    print('-='*35)
    print("A escolha do PC foi {} e a sua foi {}, logo voce Perdceu !!!".format(choice_Pc,choice_People))
    print('COMPUTADOR VENCEU')
    print('-='*35)
elif(choice_People == 1 and choice_Pc == 1) or (choice_People == 2 and choice_Pc == 2) or (choice_People == 3 and choice_Pc == 3):
    # # tratando escolha pessoa
    if choice_People == 1:
        choice_People = "Pedra"
    elif choice_People == 2:
        choice_People = "Papel"
    elif choice_People == 3:
        choice_People ="Tesoura"  
    # # Tratamento esolha pc 
    if choice_Pc == 1:
        choice_Pc = "Pedra"
    elif choice_Pc == 2:
        choice_Pc = "Papel"
    elif choice_Pc == 3:
        choice_Pc ="Tesoura" 
    print('-='*35)
    print("A escolha do PC foi {} e a sua foi {}, logo voces empataram !!!".format(choice_Pc,choice_People))
    print('EMPATOU')
    print('-='*35)
