"""9 - Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama.
"""


def its_an_anagram(word_1, word_2):

    word_1_converted = sorted(word_1.lower().strip())
    word_2_converted = sorted(word_2.lower().strip())

    if word_2_converted == word_1_converted and word_1 != word_2:
        return True
    else:
        return False


while True:
    print('A continuation ingrese dos palabras para saber\n si son un anagrama: ')
    first_word = input('\nPalabra 1: ')
    second_word = input('\nPalabra 2: ')

    print(f'El resultado fue {its_an_anagram(first_word, second_word)}')
    print(f'Por lo tanto {'si son un Anagrama' if its_an_anagram(first_word, second_word) else 'no son un Anagrama'}')

    continuar = input('\nEscriba Si para calcular nuevamente o No para salir:\n ')
    if continuar.lower() == 'no':
        print('Muchas gracias por utilizar el programa\n\n')
        break

