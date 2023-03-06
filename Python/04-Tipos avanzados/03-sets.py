"""SETS"""

# Set significa grupo o conjunto

# Set es una coleccion de datos que no se puede repetir y que tampoco esta ordenada

# Solamente puede haber uno de cada uno de los datos
# primer = {1, 1, 2, 2, 3, 4} => {1,2,3,4}
primer = {1, 2, 3, 4}

# Se puede trabjar con los sets igual que con las listas
# primer.add(5)  # {1,2,3,4,5}
# primer.remove(1)  # {2,3,4,5}

# Cualquier diterable se puede pasar a un set con la funcion set()
segundo_lista = [3, 4, 5]  # LISTA
segundo = set(segundo_lista)  # {3,4,5}

# ----------- OPERADORES DE LOS SETS ------------- #

# EL operador UNION "|" va a unir los sets eliminando cualquier elemento que se encuentre duplicado
print(primer | segundo)  # {1,2,3,4,5}

# El operador INTERSECCION "&" va a devolver los elementos que se encuentren en ambos sets
print(primer & segundo)  # {3,4}

# El operador DIFERENCIA "-" va a devolver los datos que se encuentran a
# la izquierda quitandole los que estan a la derecha
print(primer - segundo)  # {1,2}

# El operador DIFERENCIA SIMETRICA "^" va a devolver los elementos que se
# encuentren en el primero y en el segundo pero que no se encuentren enrte uno y el otro
print(primer ^ segundo)  # {1,2,5}

# ----------------------------------------------- #

# LOS SETS NO SE PUEDEN ORDENAR NI SE PUEDEN ACCEDER A ELEMENTOS DE ESTOS
# primer[2] => DEVUELVE UN ERROR

# Lo que si se puede hacer es consultar si un elemento esta dentro de un set
if 5 in segundo:
    print(True)
