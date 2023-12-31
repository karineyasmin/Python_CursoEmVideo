''' Enunciado:

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros. '''
#----------------------------------------------------------------------------------------------------
#código:
print('=-' * 30)
print('CALCULO DE DESCONTOS')
valor = float(input('\nDigite o valor do produto: R$'))
desconto = 0
print('''\nFormas de Pagamento:
            
            1 - À vista dinheiro/cheque: 10% de desconto;
            2 - À vista no cartão: 5% de desconto;
            3 - Em até 2x no cartão: preço normal;
            4 - 3x ou mais no cartão: 20% de juros ''')
opcao = int(input('\nEscolha uma das opções acima: '))

if opcao == 1:
    desconto = float((10 / valor) * 100)
    print(f'\nVocê ganhou um desconto de 10% \nO valor total é de R${valor - desconto:.2f}')
elif opcao == 2:
    desconto = float((5 / valor) * 100)
    print(f'\nVocê ganhou um desconto de 5% \nO valor total é de {valor - desconto:.2f}')
elif opcao == 3:
    print(f'\nO valor total é de {valor:.2f}')
elif opcao == 4:
    desconto = float((20 / valor) * 100)
    print(f'\nVocê terá um juros de 20% \nO valor total é de {desconto + valor:.2f}')
else:
    print('\nOpção Inválida')