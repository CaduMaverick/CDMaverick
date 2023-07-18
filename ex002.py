#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas. 

nome = input('\033[;;44m'
             'Digite seu nome: '
             '\033[m')
print('\033[;;44m'
      'É um prazer te conhecer,'
      '\033[;;43m'
      f' {nome}! '
      '\033[m')