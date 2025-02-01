## Escreva um programa que le a velociadade do carro

km_carro = int(input("Digite a Velocidade do Carro : "))

## se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
## A multa vai custar 7 por cada km acimad do limite

if(km_carro > 80):
  print("Você foi multado")
  print("Valor da Multa a ser paga é de R$ {:.2f}".format(float((km_carro - 80)*7)))
else:
  print("você nao foi multado, continue dentro do limite")
