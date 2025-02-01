 # # leia o comprimento de 3 retas e diga ao seu usurio se elas podem ou nao formar um triangulo 
 # # E diga é  Equilatgero/Isoceles/ Escaleno

reta_a = float(input("Digite o comprimento da primeira reta: "))
reta_b = float(input("Digite o comprimento da segunda reta: "))
reta_c = float(input("Digite o comprimento da terceira reta: "))

if  reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_b + reta_c > reta_a:
  print("Estes comprimentos de reta formam um triângulo.")
  if reta_a == reta_b == reta_c : # # Equilatero 
    print('Essas Retas formam um triangulo Equilatero.')

  elif reta_c != reta_a != reta_b != reta_c : # # Escaleno
    print('Essas Retas formam um triangulo Escaleno.')
  else: # # Isoceles
    print('Essas Retas formam um triangulo Isoceles .')
else:
  print("Estes comprimentos de reta NÃO formam um triângulo.")
