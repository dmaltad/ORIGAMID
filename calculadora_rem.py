import os

def calcular_rem(pixel):
    rem =pixel/16
    print(f'A conversão de {pixel}px equivale a {rem}rem.')

os.system('clear')
print('CONVERSOR DE PIXEL PARA REM\n')
px = float(input('Digite a quantidade de pixels: '))
calcular_rem(px)