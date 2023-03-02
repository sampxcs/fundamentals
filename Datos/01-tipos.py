"""Tipos de Variables"""

# --------- String ----------- #

# Backslash
# \"
# \'
# \\
# \n

STRING = "Curso de Python"

# Usa Backslashs para introducir "" en el string
DESCRIPTION = "En este curso vas a aprender todo lo necesario para programar en \"Python\""

# --------- Numbers ----------- #

NUMBER = 2  # INT
DECIMAL = 1.2  # FLOAT
IMAGINARIO = 2 + 2j  # 2 + 2i => Dos mas la raiz cuadrada de -1

# --------- Booleans ----------- #

# TRUTHY => TRUE

# FALSY => FALSE
# "" => FALSE
# 0 => FALSE
# none => FALSE

# COMPARADORES

# Mayor que: >
# Menor que: <
# Mayor o igual que: >=
# Menor o igual que: <=
# Desigualdad: !=

print(2 < 1)       # false
print(2 > 1)       # true
print(2 <= 1)      # false
print(2 + 1 == 3)  # true
print(2 + 1 != 3)  # false
print(2 == "2")    # false
print(2 != "2")    # true

# ----------- Diccionario ------------ #

# Los diccionarios se utilizan para almacenar pares clave-valor.

usuario = {
    "nombre": "Nilkarbis",  # Se colocan "Clave": "Valor" separados por comas ","
    "apellido": "Quiroz",
    "edad": 27,
}

# ----------- Listas y tuplas ------------ #

# Las listas y tuplas se utilizan para almacenar una secuencia de diferentes tipos de datos.
# Las listas se direccionan con [],
# mientras que las tuplas se direccionan con ().
# La Lista de Python es mutable mientras que las tuplas son inmutables.
# Se puede acceder a ambas listas a través de un índice.

lista = ["Hola", "Python", 3.8]  # Empieza con "[]"
lista = ("Hola", "Python", 3.8)  # Empieza con "()"

# ------------- Conjuntos -------------- #

# Los conjuntos son colecciones desordenadas de
# valores de datos únicos. Los valores de datos
# pueden ser de cualquier tipo de datos siempre
# que sean hashables e inmutables.

# Los conjuntos se pueden inicializar con valores
# de datos separados por una coma y encerrados entre llaves {}.

# Los conjuntos ignoran todos los valores repetidos
# y solo almacenan elementos únicos. Los conjuntos
# son mutables, lo que permite actualizar los valores de los datos.

conjunto = {1, 2, "Python"}
