"""
2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
"""


def calcular_hora(hora, cantidad_hs):
    return (hora+cantidad_hs) % 24


while True:
    try:
        hora_actual = int(input('Ingrese la hora actual en formato de 24hs: '))
        cantidad_horas = int(input('Ingrese cantidad de horas: '))
        print(f'\nDentro de {cantidad_horas}horas van a ser las {calcular_hora(hora_actual, cantidad_horas)}\n')
    except ValueError:
        print('Solo puede ingresar números!')

    continuar = input('Escriba Si para calcular nuevamente o No para salir ')
    if continuar.lower() == 'no':
        print('Muchas gracias por utilizar el programa')
        break
