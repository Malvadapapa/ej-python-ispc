# 1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
# número con los dígitos en orden inverso:
def num_inverter(number):
    number_string = str(number)
    auxiliar = ""
    for character in number_string:
        auxiliar = character + auxiliar
    return int(auxiliar)


while True:
    try:
        numero_a_convertir = int(input('Ingrese un numero entero de tres digitos:  '))
        print(num_inverter(numero_a_convertir))
    except ValueError:
        print('El dato ingresado no es un numero')

    finally:
        continuar = input('\nEscriba Si para calcular nuevamente o No para salir:\n ')
        if continuar.lower() == 'no':
            print('Muchas gracias por utilizar el programa\n\n')
            break




