'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''


tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade do link em Mbps: "))
velocidade_MBps = velocidade_internet / 8
tempo_segundos = tamanho_arquivo / velocidade_MBps
tempo_minutos = tempo_segundos / 60

print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")