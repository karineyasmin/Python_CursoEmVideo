'''
desafio024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO". '''
#------------------------------------------------------------------------------------------------------------------------
#código

cidade = str(input('Digite o nome da cidade que você nasceu: ')).strip() #remove os espaços por segurança

print(cidade[:5].upper() == 'SANTO') #print cidade do caracter 0 a 5(santo), convertendo pra maiuscula