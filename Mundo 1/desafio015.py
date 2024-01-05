'''
desafio015

Crie um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias de aluguel. 
Calcule o preço a pagar sabendo que o carro custa 60/dia e R$ 0,15 por km rodado. '''
#------------------------------------------------------------------------------------------------------------------------
#código

diaria_preço = 60.00
kmRodado_preço = 0.15

print('=-' * 70)

diaria = int(input('Quantos dias o veículo foi utilizado? '))
kmRodados = float(input('Quantos KM foram percorridos? '))

diariaTotal = diaria_preço * diaria
kmTotal = kmRodado_preço * kmRodados
totalValor = diariaTotal + kmTotal

print(f'\nO carro foi utilizado por {diaria} dias, cada diária custa R${diaria_preço:.2f}, com o acréscimo de R${kmRodado_preço:.2f} por KM rodado, o valor final é de R${totalValor:.2f}')
print('=-' * 70)