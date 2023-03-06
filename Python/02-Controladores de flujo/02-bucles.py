"""Bucles"""

# -------------- FOR -------------- #

for numero in range(5):  # Bucle que se ejecuta 5 veces
    print(numero)  # Devuelve una secuencia desde 0 hasta el 4

# FOR ELSE

NUMERO_A_BUSCAR = 3

for num in range(10):  # Bucle que se ejecuta 10 veces
    print(num)
    if num == NUMERO_A_BUSCAR:
        print("encontrado", NUMERO_A_BUSCAR)
        break  # Detiene la ejecucion del bucle
else:  # se ejecuta si en el bucle "for" no se llama al "break"
    print("no encontramos el numero buscado")

# FOR CON OTROS ITERABLES

for char in "Nilkarbis":
    print(char)

# BUCLES ANIDADOS

for a in range(3):
    for b in range(3):
        print(f"{a}, {b}")

# ----------- WHILE ----------- #

NUMBER = 1

while NUMBER < 100:  # Se ejecuta el bucle mientras la condicion se cumpla
    print(NUMBER)
    NUMBER *= 2  # Se multiplica el numero por 2 en cada iteracion

# HAY QUE TENER CUIDADO CON LOS LOOPS INFINITOS #
