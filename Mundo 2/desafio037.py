''' 
desafio-037
Enunciado:

Escreva um programa que leia um número qualquer e peça para o usúario escolher qual será a base de conversão:

1 - para binário
2 - para octal
3 - para hexadecimal '''
#---------------------------------------------------------------------------------------------
#código:
print('=-' * 40)
numero = input('\nDigite um número qualquer: ')
print('''\nEscolha a base de conversão:
      
      1 - para binário
      2 - para octal 
      3 - para hexadecimal 
      
      ''')
opcao = int(input(''))
if opcao == 1:
    print('\nVocê escolheu conversão para binário.')
elif opcao == 2:
    print('\nVocê escolheu conversão para octal.')
elif opcao == 3:
    print('\nVocê escolheu conversão para hexadecimal.')
else:
    print('\nOpção inválida')
print('=-' * 40)

