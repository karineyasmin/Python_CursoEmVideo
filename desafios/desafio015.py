'''
programa que pergunte a quantidade de km percorridos por um carro alugado e a qntd de dias 
pelo de aluguel. calcule o preço a pagar sabendo que o carro custa 60/dia e R$ 0,15 por km rodado 
'''

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