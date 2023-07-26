# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input('Digite algo: ')

print(f'O Tipo primitivo desse valor é {type(var)}\n'
      f'Contem somente letras? {var.isalpha()}\n'
      f'Contem somente números? {var.isnumeric()}\n'
      f'Contem um dos dois? {var.isalnum()}\n'
      f'É completamente em minúsculo? {var.islower()}\n'
      f'Contem somente espaços? {var.isspace()}\n'
      f'Está capitalizado? {var.istitle()}\n')