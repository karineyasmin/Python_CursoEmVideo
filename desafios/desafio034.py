''' escreva um programa que pergunte o salario de um funcionario e calcule o valor 
do seu aumento

para salarios superiores a R$ 1.250,00, calcule um aumento de 10%

para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Digite o salário: '))

if salario > 1250.00:
    salario = (salario * 0.10) + salario
    print(f'Seu salário terá um aumento será de 10%.\n Seu novo salário é de {salario:.2f}')
else:
    salario = (salario * 0.15) + salario
    print(f'Seu salário terá um aumento será de 15%.\n Seu novo salário é de {salario:.2f}')
