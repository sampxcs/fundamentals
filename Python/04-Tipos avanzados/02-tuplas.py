"""TUPLAS"""

# Las tuplas son iguales a las listas con la unica diferencia que no se pueden modificar
# aunque si se pueden crear nuevas tuplas a partir de otras
# Se puedes realizar todas las operacion que se utilizan en las listas menos las de modificar

# Las tuplas se escriben entre "()"

numeros = (1, 2, 3, 4, 5, 6)
print(numeros[2])  # 3
print(numeros[:2])  # (1 , 2)

# tuple() resive cualquier dato iterable y lo combierte en tupla
punto = tuple([1, 2])

# Si quieres modificar una tupla deberas crear una lista a partir de esa tupla y
# ahi si modificarla

# Devuelve una lista en base a la tupla de numeros
numeros_lista = list(numeros)

numeros_lista.pop()  # Elimina el ultimo elemento de la lista
