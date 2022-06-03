__author__ = 'Camilly'

print('====================================')

salario = float(input('Digite seu salário: ').replace(',','.'))
porc = float(input('Digite a porcentagem do aumento: ').replace(',','.'))
porc = porc/100

novosal = salario * porc + salario
print('O seu salário novo é: R$%.2f '%novosal)
