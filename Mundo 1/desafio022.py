'''
desafio022
Crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maiúsculas;
- todas minúsculas;
- quantas letras ao todo (sem considerar espaços);
- quantas letras tem o primeiro nome. '''
#------------------------------------------------------------------------------------------------------------------------
#código

nome = str(input('Digite seu nome completo: '))
maius = nome.upper()
minus = nome.lower()
sem_esp = nome.replace(' ', '')
primeiro = nome.split()

print(f'\ntodas maiúsculas: {maius}')
print(f'\ntodas minúsculas: {minus}')
print(f'\nSeu nome tem {len(sem_esp)} letras, sem considerar os espaços')
print(f'\nSeu primeiro nome é {primeiro[0]} e tem ele tem {len(primeiro[0])} letras')

