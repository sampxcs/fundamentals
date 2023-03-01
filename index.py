"""INDEX"""
import math  # Modulo nativo que podemos importar para tener mas funciones con numeros

# BACKSLASH
# \"
# \'
# \\
# \n

## VARIABLES ##

TITLE = "Curso de Python"
TEXT = "hola mundo"
DESCRIPTION = "en este curso vas a aprender todo lo necesario para programar en \"Python\""

print(f"{TITLE} {TEXT}")
print(DESCRIPTION)
print(TEXT[0:4])

## METODOS DE STRINGS ##

print(len(TEXT))
print(TEXT.upper())
print(TEXT.lower())
print(TEXT.strip().capitalize())
print(TEXT.title())
print(TEXT.strip())
print(TEXT.lstrip)
print(TEXT.rstrip())
print(TEXT.find("mundo"))
print(TEXT.replace("mundo", "nikki"))
print("mundo" in TEXT)
print("mundo" not in TEXT)

# NUMEROS
# TIPOS

NUMBER = 2  # INT
DECIMAL = 1.2  # FLOAT
IMAGINARIO = 2 + 2j  # 2 + 2i => Dos mas la raiz cuadrada de -1

# OPERACIONES ARICMETICAS

NUMBER += 2  # NUMBER = NUMBER + 2
NUMBER -= 2  # NUMBER = NUMBER - 2
NUMBER *= 2  # NUMBER = NUMBER * 2
NUMBER /= 2  # NUMBER = NUMBER / 2

print(1 + 3)
print(1 - 3)
print(1 * 3)
print(1 / 3)
print(1 // 3)  # Division sin decimales
print(1 % 3)   # Devuelve el resto de la division
print(2 ** 3)  # Exponente

# FUNCIONES DE NUMEROS

print(round(2.3))  # Redondea a 2
print(abs(-77))  # Valor absoluto => siempre es positivo

# MATH

print(math.ceil(1.6))  # Redondea hacia arriba
print(math.floor(1.6))  # Redondea hacia abajo
print(math.pow(23, 3))  # Eleva a la potencia
print(math.sqrt(2))  # Raiz cuadrada

## DATOS BOOLEANOS ##

# TRUTHY => TRUE

# FALSY => FALSE
# ""
# 0
# none

# COMPARADORES

print(2 < 1)       # false
print(2 > 1)       # true
print(2 <= 1)      # false
print(2 + 1 == 3)  # true
print(2 + 1 != 3)  # false
print(2 == "2")    # false
print(2 != "2")    # true

## CONDICIONALES ##

EDAD = 22

# IF ELIF ELSE

if EDAD > 65:  # Si cumple con la condicion se ejecuta el codigo a continuecion
    print("Es mayor de 65 años")
elif EDAD > 18:  # Si no, si cumple con la condicion se ejecuta el codigo a continuecion
    print("Es mayor de 18 años")
else:  # Si no se cumple las condiciones se ejecutara el codigo a continuacion
    print("Es menor de 18 años")

# OPERADOR TERNARIO

MENSAJE = "Es mayor de 18 años" if EDAD > 18 else "Es menor de 18 años"

print(MENSAJE)

# OPERADORES LOGICOS
# and, or, not => "SI", "O", "NO"

LOGIN = False
PAGO = True

if LOGIN and PAGO:
    print("Puedes continuar")

if not LOGIN or not PAGO:
    print("No puedes continuar")

# CADERA DE COMPARACIONES

if 18 <= EDAD <= 65:
    print("Tiene entre 18 y 65 años")

## BUCLES ##

# FOR

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

# WHILE

NUMBER = 1

while NUMBER < 100:  # Se ejecuta el bucle mientras la condicion se cumpla
    print(NUMBER)
    NUMBER *= 2  # Se multiplica el numero por 2 en cada iteracion

# HAY QUE TENER CUIDADO CON LOS LOOPS INFINITOS #

# BUCLES ANIDADOS

for a in range(3):
    for b in range(3):
        print(f"{a}, {b}")
