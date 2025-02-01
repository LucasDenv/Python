## Pergunte a distancia de uma viagem (km)
km_viagem = int(input("Qual a kilometragem dessa viagem ?"))
## Calcule o preço da passagem, 0,50 por km para viagens de are 200km
if (km_viagem > 200):
  print("O valor da sua viagem é R${:.2f}".format(float(km_viagem*1/2)))
## 0,45 para viagens mais longas 
else :
  print("O valor da sua viagem é R${:.2f}".format(float(km_viagem*45/100)))
