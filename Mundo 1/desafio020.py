''' 
desafio020
Um professor quer sortear a ordem de apresentação de trabalhos dos alunos,
faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''
#------------------------------------------------------------------------------------------------------------------------
#código

from random import shuffle

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1,n2,n3,n4]
shuffle(lista)  

print('A ordem de apresentação será: ')             
print(lista)
               
 
 
 