#desafio013 
# Crie um algortimo que lê o salário de um funcionário e mostra seu novo salário com 15% de aumento.

#CODIGO:

salario = float(input('Digite o salário: '))

aumento = (salario * 15) / 100

salario_final = salario + aumento 

print(f'\nCom o aumento de 15%, o novo salário será: {salario_final}')