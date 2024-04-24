"""
7- La secuencia de Collatz de un número entero se construye de la siguiente forma:
● si el número es par, se lo divide por dos;
● si es impar, se le multiplica tres y se le suma uno;
● La sucesión termina al llegar a uno.
Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
"""


def even_action(number):
    return number/2


def odd_action(number):
    return (number*3) + 1


def collatz_calculator(integer_number):
    auxiliar = []
    while True:
        auxiliar.append(int(integer_number))

        if integer_number == 1:
            break
        elif integer_number % 2 == 0:
            integer_number = even_action(integer_number)
        else:
            integer_number = odd_action(integer_number)

    return auxiliar


while True:
    try:
        selected_number = int(input('Ingrese un numero para imprimir su respectiva \n secuencia de collatz: '))
        print(f'La lista es {collatz_calculator(selected_number)}')

    except ValueError:
        print('El valor ingresado debe ser un numero entero!')

    finally:
        continuar = input('\nEscriba Si para calcular nuevamente o No para salir:\n ')
        if continuar.lower() == 'no':
            print('Muchas gracias por utilizar el programa\n\n')
            break

