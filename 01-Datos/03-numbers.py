"""Numbers"""

import math  # Modulo nativo que podemos importar para tener mas funciones con numeros

NUMBER = 2  # INT
DECIMAL = 1.2  # FLOAT
IMAGINARIO = 2 + 2j  # 2 + 2i => Dos mas la raiz cuadrada de -1

# ---------- OPERACIONES ARICMETICAS ------------ #

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

# ---------- FUNCIONES DE NUMEROS ------------ #

print(round(2.3))  # Redondea a 2
print(abs(-77))  # Valor absoluto => siempre es positivo

# MATH

print(math.ceil(1.6))  # Redondea hacia arriba
print(math.floor(1.6))  # Redondea hacia abajo
print(math.pow(23, 3))  # Eleva a la potencia
print(math.sqrt(2))  # Raiz cuadrada
