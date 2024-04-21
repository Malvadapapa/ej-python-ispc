# 1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
# número con los dígitos en orden inverso:
def num_inverter(number):
    number_string = str(number)
    auxiliar = ""
    for character in number_string:
        auxiliar = character + auxiliar
    return int(auxiliar)


loop_control = True

while loop_control:
    try:
        numero_a_convertir = int(input('Ingrese un numero entero de tres digitos:  '))
        print(num_inverter(numero_a_convertir))

        while True:
            exit_while = input('\nEscriba si para convertir otro numero o no para salir: ')
            if exit_while.lower() == 'no':
                print('Gracias por utilizar el programa')
                loop_control = False
                break
            else:
                break

    except ValueError:
        print('El dato ingresado no es un numero')



