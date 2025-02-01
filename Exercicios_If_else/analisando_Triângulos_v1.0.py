## leia o comprimento de 3 retas e diga ao seu usurio se elas podem ou nao formar um triangulo 
reta_a = float(input("Digite o comprimento da primeira reta: "))
reta_b = float(input("Digite o comprimento da segunda reta: "))
reta_c = float(input("Digite o comprimento da terceira reta: "))

if  reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_b + reta_c > reta_a:
  print("Estes comprimentos de reta formam um triângulo.")
else:
  print("Estes comprimentos de reta NÃO formam um triângulo.")
