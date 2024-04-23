"""
4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
"""


def calcular_horas_viaje(minutos):
    horas = int(minutos / 60)
    minutos = minutos % 60
    hora_final = str(horas).zfill(2) + ':' + str(minutos).zfill(2)

    return hora_final


while True:
    print('Ingrese los tiempos en minutos que \nduraron los tramos de su viaje:\n')
    minutos_totales = 0
    contador_tramo = 1

    while True:
        minutos_viaje = int(input(f'Ingrese tramo {contador_tramo}:'))
        minutos_totales += minutos_viaje
        contador_tramo = contador_tramo + 1

        if minutos_viaje == 0:
            break

    print(f'La cantidad de horas de viaje es: {calcular_horas_viaje(minutos_totales)}')
    continuar = input('Escriba Si para calcular nuevamente o No para salir:\n ')
    if continuar.lower() == 'no':
        print('Muchas gracias por utilizar el programa\n\n')
        break
