import os

def limpar_tela():
    os.system('clear')

def texto_inicial():
        print('''
CONVERSOR DE PIXEL PARA REM
              
    1. Converter Pixel para Rem
    2. Converter Rem para Pixel
    3. Sair
          
''')
        
def continuar():
    a = input('Digite alguma coisa para seguir: ')

def calcular_rem():
    limpar_tela()
    try:
        pixel = float(input('Digite a quantidade de pixels: '))
    except:
        print('Valor inválido, tente novamente.\n')
        continuar()
        calcular_rem()
    rem =pixel/16
    print()
    print(f'A conversão de {pixel}px equivale a {rem}rem.')
    continuar()
    main()

def calcular_pixel():
    limpar_tela()
    try:
        rem = float(input('Digite a quantidade de rem: '))
    except:
        print('Valor inválido, tente novamente.\n')
        continuar()
        calcular_rem()
    pixel =rem*16
    print()
    print(f'A conversão de {rem}rem equivale a {pixel}pixel.')
    continuar()
    main()


def opcoes():
    try:
        opcao = int(input('Digite uma opção: '))
        
        match opcao:
            case 1:
                calcular_rem()
            case 2:
                calcular_pixel()
            case 3:
                print('Encerrando...')
    except:
        print('Opção inválida, tente novamente.\n')
        continuar()
        main()
        
def main():
    limpar_tela()
    texto_inicial()
    opcoes()


if __name__ == '__main__':
    main()