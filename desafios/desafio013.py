#desafio013 algortimo que leia o salario de um funcionario e mostr seu novo salario com 15% de aumento

salario = float(input('Digite o salário: '))
aumento = (salario * 15) / 100
salario_final = salario + aumento 

print(f'\nCom o aumento de 15%, o novo salário será: {salario_final}')