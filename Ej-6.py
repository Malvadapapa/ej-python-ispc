"""
6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario.

"""


def triangle_generator(n_iteraciones, multiplo=2):
    for n_columna in range(1, n_iteraciones + 1):
        string_fila = ""
        for n_fila in range(1, n_columna + 1):
            string_fila += str(multiplo * n_fila) + ' '
        print(string_fila)


while True:
    try:
        n_filas = int(input('Ingrese numero de filas del triangulo: '))
        triangle_generator(n_filas)

    except ValueError:
        print('El valor ingresado no es un numero!')

    continuar = input('\nEscriba Si para calcular nuevamente o No para salir:\n ')
    if continuar.lower() == 'no':
        print('Muchas gracias por utilizar el programa\n\n')
        break

