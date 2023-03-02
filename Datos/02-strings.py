"""Strings"""

TITLE = "Curso de Python"
TEXT = "hola mundo"
DESCRIPTION = "en este curso vas a aprender todo lo necesario para programar en \"Python\""

# Con f"" se puede aceder a variables dentro de un string

print(f"{TITLE} {TEXT}")  # Inicia con "f" y coloca las variables dentro de {}

# Puedes acceder a los indices de un string colocando []
# y dentro el numero del indice que quieres acceder

# Los indices empiezan en "0"

print(TITLE[3])  # Corresponde a la letra "s"

# Puedes separar una parte del string colocanto
# dos indices separados por ":"

# devolvera los indices desde el primer numero hasta el segundo

print(TEXT[0:4])  # Devuelve "hola"

print(len(TEXT))  # Devuelve la longutud del string

# --------------- Metodos de strings -------------- #

# upper() Devuelve el string en MAYUSCULAS
print("upper():", TEXT.upper())  # HOLA MUNDO

# lower() Devuelve el string en minusculas
print("lower():", TEXT.lower())  # hola mundo

# capitalize() Primera letra en MAYUSCULAS y el resto en minusculas
print("capitalize():", TEXT.capitalize())  # Hola mundo

# capitalize() Primera letra de cada palabra en MAYUSCULAS
print("title():", TEXT.title())  # Hola Mundo

# strip() Elimina los espacios a los lados
print("strip():", TEXT.strip())  # hola mundo

# lstrip() Elimina los espacios a la izquierda
print("lstrip():", TEXT.lstrip())  # hola mundo

# rstrip() Elimina los espacios a la derecha
print("rstrip():", TEXT.rstrip())  # hola mundo

# find() Busca la palabra y devuelve el indice donde empieza
print("find():", TEXT.find("mundo"))  # 5

# rfind() Busca y devuelve el indice donde termina
print("rfind():", TEXT.rfind("mundo"))  # 10

# replace() Reemplaza la palabra 1 por la 2
print("replace():", TEXT.replace("mundo", "nikki"))  # hola nikki

# in Busca la palabra y devuelve un booleano
print("in:", "mundo" in TEXT)  # True

# not in Busca si NO esta palabra y devuelve un booleano
print("not in:", "mundo" not in TEXT)  # False

# count() Devuelve el numero de veces que se repite "hola"
print("count():", TEXT.count("hola"))  # 1

# startswith() Devuelve TRUE si el string EMPIEZA con "hola"
print("startswith():", TEXT.startswith("hola"))  # True

# endswith() Devuelve TRUE si el string TERMINA con "hola"
print("endswith():", TEXT.endswith("hola"))  # False

# isdigit() Determinan si los caracteres del string son dígitos
print("isdigit():", TEXT.isdigit())  # False

# join(iterable) es usado para unir todos los
# elementos de un iterable con un espefico string str in Python.
# Si, el iterable no contiene ningún valor en los strings,
# Esto conduce a un TypeError exception.

print("join()", " y ".join(["A", "B", "C"]))  # "A y B y C"

# center(), ljust() y rjust() alinean una cadena en el centro,
# la izquierda o la derecha respectivamente. Toman un argumento, la cantidad
# de caracteres respecto de la cual se producirá la alineación.

print("center()", TEXT.center(10))  # '   hola mundo   '
print("center()", TEXT.ljust(10))   # '      hola mundo'
print("center()", TEXT.rjust(10))   # 'hola mundo      '

# swapcase() cambia las mayúsculas por minúsculas y viceversa.
print("swapcase()", TEXT.swapcase())  # "HOLA MUNDO"

# split() divide un string según un caracter separador,
# cuyo separador por defecto son espacios en blanco y saltos de línea.

print("split()", TEXT.split())  # ['hola', 'mundo']
print("split()", TEXT.split("o"))  # ['h', 'la mund', '']
