"""EJERCICIOS"""

# Crea una funcion que devuelva True si el texto ingresado es
# un palindromo y False si no lo es

# ------------------------------------------------ #
#                EJERCICIO RESUELTO                #
# ------------------------------------------------ #


def es_palindromo(string):
    """FUNCION QUE NOS DICE SI UNA PALABRA ES UN PALINDROMO"""
    string = string.replace(" ", "").lower()
    result = ""

    index = len(string) - 1

    while index >= 0:
        result += string[index]
        index -= 1

    return result == string


print(es_palindromo("abba"))
print(es_palindromo("Reconocer"))
print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola mundo"))
