''' 
desafio-039
Enunciado:

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''
#-----------------------------------------------------------------------------------------------------------------------------
#código
print('=-' * 40)
idade = int(input('Digite a sua idade: '))

if idade <= 17:
    print('\nVocê ainda se alistará ao serviço militar!')
elif idade == 18:
    print('\nEstá na hora do seu alistamento militar!')
else:
    atraso = idade - 18
    print(f'\nJá se passaram {atraso} ano(s) do seu alistamento. ')      
print('=-' * 40)   