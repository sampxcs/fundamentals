"""Funciones"""

# CREAR UNA FUNCION


def funcion():
    """My Function"""
    return "Hola desde una funcion"


print(funcion())

# FUNCIONES CON PARAMENTROS


def funcion_con_un_parametro(texto):
    """My Function"""
    print(texto)


funcion_con_un_parametro("Hola desde una funcion con un parametro")


def funcion_con_varios_parametros(text01, text02):
    """My Function"""
    print(text01, text02)


funcion_con_varios_parametros(
    "Hola desde", "una funcion con varios parametros")

# FUNCIONES CON PARAMENTROS OPCIONALES


def funcion_con_varios_parametros_opcionales(text01="Hola", text02="Mundo"):
    """My Function"""
    print(text01, text02)


funcion_con_varios_parametros_opcionales("Buenos dias")

# FUNCIONES CON INFINITOS PARAMENTROS


def suma_con_infinitos_parametros(*numeros):
    """My Function"""
    resultado = 0
    for nume in numeros:
        resultado += nume
    return resultado


print(suma_con_infinitos_parametros(2, 3, 5))
print(suma_con_infinitos_parametros(2, 5))
print(suma_con_infinitos_parametros(2, 5, 8, 15))

# FUNCIONES CON UN PARAMENTRO CON PROPIEDADES


def funcion_con_un_diccionario_como_parametro(**usuario):
    """My Function"""
    print(usuario)
    print(usuario["nombre"], usuario["apellido"])


funcion_con_un_diccionario_como_parametro(nombre="Ian", apellido="Rosales")
