''' 
desafio044
Enunciado:

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros. '''
#----------------------------------------------------------------------------------------------------
#código:
print('=-' * 18)
print('\tLOJA DA PÍTON')
print('=-' * 18)
preço = float(input('Preço total da compra: R$'))
print('''\nFormas de Pagamento:
            
1 - À vista dinheiro/cheque: 10% de desconto;
2 - À vista no cartão: 5% de desconto;
3 - Em até 2x no cartão: preço normal;
4 - 3x ou mais no cartão: 20% de juros ''')
opcao = int(input('\nQual a opção de pagamento? '))

if opcao == 1:
    total = preço - (preço * 10 / 100) 
    print(f'\nVocê ganhou um desconto de 10%.')
elif opcao == 2:
    total = preço - (preço * 5 / 100)
    print(f'\nVocê ganhou um desconto de 5%.')
elif opcao == 3:
    total = preço
    parcela = preço / 2 
    print(f'\nSua compra será parcelada em 2x de {parcela} SEM JUROS')
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totalParcelas = int(input('Quantas Parcelas? '))
    parcela = total / totalParcelas
    print(f'Sua compra será parcelada em {totalParcelas}x de R${parcela:.2f} COM JUROS')
else:
    total = preço
    print('\nOpção Inválida de pagamento')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
