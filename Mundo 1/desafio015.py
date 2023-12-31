#desafio015

'''
Crie um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias de aluguel. 
Calcule o preço a pagar sabendo que o carro custa 60/dia e R$ 0,15 por km rodado.
'''

#CODIGO:

diaria_preço = 60.00
kmRodado_preço = 0.15

print('-' * 40)

diaria = int(input('Quantos dias o veículo foi utilizado? '))
kmRodados = float(input('Quantos KM foram percorridos? '))

diariaTotal = diaria_preço * diaria
kmTotal = kmRodado_preço * kmRodados
totalValor = diariaTotal + kmTotal

print(f'\nO carro foi utilizado por {diaria} dias, cada dia custa {diaria_preço}, com o acréscimo de {kmRodado_preço} por KM rodado, o valor final é de {totalValor}')
print('-' * 40)