"""LISTAS"""

numeros = [1, 2, 3, 4, 5, 6]
letras = ["a", "b", "c", "d"]
matriz = [[1, 2], [1, 2]]
ceros = [0] * 10  # [0,0,0,0,0,0,0,0,0,0]
alfanumericos = letras + numeros  # ["a","b","c","d", 1,2,3,4,5,6]
rango = list(range(1, 10))  # [1,2,3,4,5,6,7,8,9,10]
chars = list("hola mundo")  # ["h","o","l","a","","m","u","n","d","o"]
mascotas = ["gato", "perro", "ave", "hamster"]

# ----------------- ACCEDER Y MODIFICAR VALORES -------------------- #

print(mascotas[1])      # "perro"
mascotas[1] = "caballo"  # Cambiando el valor del elemento 1
print(mascotas[1])      # "caballo"

print(mascotas[0:2])    # ["gato", "caballo"]
print(mascotas[1:])     # ["caballo", "ave", "hamster"]
print(mascotas[-1])     # "hamster"
print(mascotas[::2])    # ["gato", "ave"]
print(mascotas[1::2])   # ["caballo", "hamster"]

# -------------------- DESEMPAQUETAR LISTAS ----------------------- #

# Crea 6 variables con los valores de la lista de numeros
uno, dos, tres, cuatro, cinco, seis = numeros

# Crea una variable solo con el primer elemento de una lista y otra
# que sera una lista con los elementos restantes
primero, *otros = letras  # "a" ["b","c","d"]
primero, segundo, *otros = letras  # "a" "b" ["c","d"]
primero, *otros, ultimo = letras  # "a" ["b","c"] "d"

# ----------------------- ITERANDO LISTAS ----------------------- #

for mascota in mascotas:
    print(mascota)  # Lista con el nombre de cada mascota

# enumerate() devuelve una tupla con el indice y el nombre de la mascota
for mascota in enumerate(mascotas):
    print(mascota)  # indice y nombre de mascota

# Desempaquetando el indice de la tupla para tener los valores separados
for index, mascota in enumerate(mascotas):
    print(index, mascota)  # indice por un lado y del otro el nombre

# --------------------- BUSCAR ELEMENTOS ----------------------- #

# index() devuelve el indice del primer elemento encontrado que se quiere buscar
# sino lo encuentra devuelve un error

if "caballo" in mascotas:
    print(mascotas.index("caballo"))  # 1

# --------------- AGREGAR Y ELIMINAR ELEMENTOS ---------------- #

# Con insert() podemos agregar elementos a una lista indicandole primero el
# indice donde lo queremos agregar y despues del valor
mascotas.insert(1, "perro")  # ["gato", "perro", "caballo", "ave", "hamster"]

# append() agrega un elemento al final de una lista
mascotas.append("caballo")
# ["gato", "perro", "caballo", "ave", "hamster","caballo"]

# count() devuelve las veces que se repite un elemento en una ista
mascotas.count("caballo")  # 2

# remove() elimina el primer elemento encontrado
mascotas.remove("caballo")  # ["gato", "perro", "ave", "hamster","caballo"]

# pop() si no le pasas ningun indice elimina el ultimo elemento
# si le pasas un indice elimina ese elemento
mascotas.pop()  # ["gato", "perro", "ave", "hamster"]
mascotas.pop(1)  # ["gato", "ave", "hamster"]

# La palabra reservada "del" elimina el elemento seleccionado
del mascotas[0]  # ["ave", "hamster","caballo"]

# clear() limpia toda la lista
mascotas.clear()  # []

# --------------- ORDENAR UNA LISTA ----------------- #

numeros_desordenados = [1, 6, 4, 7, 3, 2]

# sort() ordena la lista en orden acendente y con el parametro "reverse" la ordena
# en orden desendente
numeros_desordenados.sort()  # [1,2,3,4,6,7]
numeros_desordenados.sort(reverse=True)  # [7,6,4,3,2,1]

# sorted() devuelve una nueva lista con los numeros ordenados
# tambien resive el parametro "reverse"
numeros_ordenados = sorted(numeros_desordenados)  # [1,2,3,4,6,7]
numeros_ordenados = sorted(numeros_desordenados, reverse=True)  # [7,6,4,3,2,1]

# ORDENANDO ELEMENTOS MAS COMPLEJOS

# En este caso toma el primer elemento de cada lista para ordenarlo
usuarios = [[3, "samuel"], [1, "alex"], [5, "nilkar"]]
usuarios.sort()  # [[1, "alex"], [3, "samuel"], [5, "nilkar"]]

# Para indicarle a sort() como debe ordenar los elementos debemos pasarle una funcion
usuarios = [["samuel", 3], ["alex", 1], ["nilkar", 5]]


def funcion_para_ordenar(elemento):
    # se debe retornar el elemento que debe tomar para ordenar
    return elemento[1]


# [["alex", 1], ["samuel", 3], ["nilkar", 5]]
usuarios.sort(key=funcion_para_ordenar)

# [["nilkar", 5], ["samuel", 3], ["alex", 1]]
usuarios.sort(key=funcion_para_ordenar, reverse=True)

# ------------------ FUNCIONES LAMBDA ------------------ #

# Lo anterior se puede simplificar usando una funcion lambda
# La funcion lambda resive el y retorna un valor "lambda elemento: elemento_a_retornar"

# [["alex", 1], ["samuel", 3], ["nilkar", 5]]
usuarios.sort(key=lambda el: el[1])

# [["nilkar", 5], ["samuel", 3], ["alex", 1]]
usuarios.sort(key=lambda el: el[1], reverse=True)

# --------------- COMPRENCION DE LISTAS ------------------ #

# Para crear una lista basada en otra diferente podemos hacer lo siguiente

nombres_de_usuarios = []
for usuerio in usuarios:
    nombres_de_usuarios.append(usuerio[0])
# ["nilkar", "samuel", "alex"]


# Pero podemos usar la comprencion de listas para hacerlo de la siguiente manera
# lista = [expresion for item in items]

nombres_de_usuarios = [usuerio[0] for usuario in usuarios]
# ["nilkar", "samuel", "alex"]

# Para FILTRAR una lista:
usuarios_con_id_mayor_a_2 = [usuerio for usuerio in usuarios if usuerio[1] > 2]
# [["nilkar, 5"], ["samuel", 3]]

# Para MODIFICAR y FILTRAR:
nombres_de_usuarios = [usuerio[0] for usuario in usuarios if usuerio[1] > 2]
# ["nilkar", "samuel"]

# -------------------- MAP Y FILTER --------------------- #

# Alternativas a la comprencion de listas son MAP() y FILTER()

# Para MODIFICAR usa map()
nombres_de_usuarios = list(map(lambda usuario: usuario[0], usuarios))
# ["nilkar", "samuel", "alex"]

# Para FILTRAR usa filter()
usuarios_con_id_mayor_a_2 = list(
    filter(lambda usuario: usuario[1] > 2, usuarios))
