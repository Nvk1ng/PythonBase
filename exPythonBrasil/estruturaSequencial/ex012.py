'''Tendo como dados de entrada um arquivo em Gigabytes, 
construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:
Gigabytes * 1024
'''

gigabyte = int(input("Digite o tamanho do arquivo em gigabytes para converter para megabytes:"))
conversao = gigabyte * 1024

print(f"O arquivo tem {conversao} MBs")