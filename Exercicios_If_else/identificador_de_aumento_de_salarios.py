## Pergunte o salario de um funcionario e calcule o valor do seu aumento
salario = float(input("Informe seu Salário para calcularmos o seu aumento: "))
## PAra os inferiores ou iguais o aumento sera de 15%
if(salario<=1250):
  salario = salario + (salario*15)/100
  print("Seu aumento é de 15% seu salario passou a ser R$ {:.2f}".format(salario))
## salarios superiores a 1250, calcule um aumentio de 10%
else: 
  salario = salario + (salario*10)/100
  print("Seu aumento é de 10% seu salario passou a ser R$ {:.2f}".format(salario))
