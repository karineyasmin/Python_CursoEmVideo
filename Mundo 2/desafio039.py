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
from datetime import date

print('=-' * 20)
anoAtual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento
print(f'Quem naceu em {nascimento} tem {idade} anos em {anoAtual}.')

if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    prazo = 18 - idade
    ano = anoAtual + prazo
    print(f'Você ainda não tem 18 anos, ainda faltam {prazo} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    prazo = idade - 18
    ano = anoAtual - prazo
    print(f'Você já deveria ter se alistado há {prazo} anos.')
    print(f'Seu ano de alistamento foi em {ano}')