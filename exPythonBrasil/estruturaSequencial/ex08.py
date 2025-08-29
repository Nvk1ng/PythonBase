'''Faça um programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
'''

salarioPorHora = float(input("Quanto voce ganha por hora:"))
horasTrabalhadas = int(input("Quantas horas voce trabalhou esse mes:"))
salario = salarioPorHora * horasTrabalhadas

print(f"O seu  salario esse mes é de {salario}")