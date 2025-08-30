'''
João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''



LIMITE = 50
VALOR_MULTA = 4.0


peso = float(input("Digite o peso de peixes trazido por João (em kg): "))


if peso > LIMITE:
    excesso = peso - LIMITE
    multa = excesso * VALOR_MULTA
else:
    excesso = 0
    multa = 0


print(f"Peso total de peixes: {peso} kg")
print(f"Excesso de peso: {excesso} kg")
print(f"Valor da multa: R$ {multa:.2f}")
