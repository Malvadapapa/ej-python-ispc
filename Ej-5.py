"""
5- Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido
exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la
diferencia es de más o menos un cuarto de día.
Para evitar que las estaciones se desfasen con el calendario, el calendario juliano
introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados
bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.
Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente
3/400 de día.
Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo
calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que
fuera divisible por 400.
Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era
el calendario vigente en ese año:
2

1- si el año es divisible por cero debe ser bisiesto antes de la reforma gregoriana
2- luego de la reforma gregoriana si el número es divisible por 100 es el último del siglo
a su vez si este es divisible por 400 significa que es bisiesto


"""


def leap_year_calculator(current_year):
    if current_year < 1582:
        if current_year % 4 == 0:
            return 'es bisiesto'
        else:
            return 'no es bisiesto'
    else:
        if (current_year % 100 == 0 and current_year % 400 == 0) or (current_year % 4 == 0 and current_year % 100 != 0):
            return 'es bisiesto'
        else:
            return 'no es bisiesto'


while True:
    try:
        selected_year = int(input('Ingrese un año para averiguar si es bisiesto o no:  '))
        print(f'\nEl año {selected_year} {leap_year_calculator(selected_year)}')
    except ValueError:
        print('Debe ingresar un numero entero!')

    continuar = input('\nEscriba Si para calcular nuevamente o No para salir:\n ')
    if continuar.lower() == 'no':
        print('Muchas gracias por utilizar el programa\n\n')
        break

