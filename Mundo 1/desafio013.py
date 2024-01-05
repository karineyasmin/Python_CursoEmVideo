'''
desafio013 

Crie um algoritmo que leia o salário de um funcionário e mostra seu novo salário com 15% de aumento. '''
#------------------------------------------------------------------------------------------------------------------------
#código

salario = float(input('Digite o salário: R$'))
aumento = (salario * 15) / 100
salario_final = salario + aumento 

print(f'\nCom o aumento de 15%, o novo salário será de R${salario_final:.2f}')