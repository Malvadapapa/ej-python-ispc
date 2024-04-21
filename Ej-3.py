"""
3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.

¿Qué son los números primos? Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1,
es decir, que si intentamos dividirlos por cualquier otro número, el resultado no es entero. Dicho de otra forma,
si haces la división por cualquier número que no sea 1 o él mismo, se obtiene un resto distinto de cero.

Método para averiguar si un número es primo(criba de Erastostenes):
https://www.youtube.com/watch?v=9vhJ8jplsgw&ab_channel=DanielCarre%C3%B3n
"""


def calcular_primo(number):
    if number <= 1:
        return False
    contador = 2
    while contador * contador <= number:
        if number % contador:
            contador = contador + 1

        else:
            return False
    else:
        return True


while True:
    numero = int(input('Ingrese un numero para averiguar si es primo: '))
    if calcular_primo(numero):
        print(f'Si el numero {numero} es primo')
    else:
        print(f'No el numero {numero} no es primo')

    continuar = input('Escriba Si para calcular nuevamente o No para salir ')
    if continuar.lower() == 'no':
        print('Muchas gracias por utilizar el programa')
        break
