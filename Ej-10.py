def string_to_list(lista):
    auxiliar = lista.split()
    for i in range(len(auxiliar)):
        auxiliar[i] = int(auxiliar[i])
    return auxiliar

def quien_captura(torre, alfil):
    torre = string_to_list(torre)
    alfil = string_to_list(alfil)

    if abs(torre[0] - alfil[0]) == abs(torre[1] - alfil[1]):
        return print('Alfil captura a torre')
    elif torre[0] == alfil[0] or torre[1] == alfil[1]:
        return print('Torre captura a Alfil')
    else:
        return print('Ninguna pieza captura')


print('Ingresa dos números separados por un espacio\n para las posiciones del alfil y la torre:')
tower_position =  input('Posicion torre:')
alfil_position =  input('posicion alfil:')

quien_captura(tower_position,alfil_position)

